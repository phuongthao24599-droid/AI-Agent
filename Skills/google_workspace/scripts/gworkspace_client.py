#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Google Workspace Unified Client Script
Quản lý các dịch vụ Google Workspace: Gmail, Calendar, Drive, Sheets, Docs.
Hỗ trợ OAuth 2.0 Desktop Application & Service Account.
"""

import os
import sys
import json
import argparse
from datetime import datetime

# Thiết lập encoding UTF-8 cho Windows console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Đường dẫn gốc dự án
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CREDENTIALS_DIR = os.path.join(PROJECT_ROOT, "Credentials")
LOGS_DIR = os.path.join(PROJECT_ROOT, "Logs")

def log_action(action_name, status, details):
    """Ghi nhận nhật ký hoạt động vào thư mục Logs/ theo quy chuẩn ISO 8601."""
    os.makedirs(LOGS_DIR, exist_ok=True)
    log_file = os.path.join(LOGS_DIR, f"gworkspace_{datetime.now().strftime('%Y-%m')}.log")
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "action": action_name,
        "status": status,
        "details": details
    }
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

class GoogleWorkspaceClient:
    def __init__(self, creds_path=None):
        self.creds_path = creds_path or self._find_credentials()
        self.services = {}
        
    def _find_credentials(self):
        """Tìm kiếm file cấu hình xác thực trong Credentials/."""
        possible_paths = [
            os.path.join(CREDENTIALS_DIR, "google_workspace_credentials.json"),
            os.path.join(CREDENTIALS_DIR, "service_account.json"),
            os.path.join(CREDENTIALS_DIR, "credentials.json")
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None

    def _get_service(self, service_name, version):
        """Khởi tạo Google API Service."""
        if service_name in self.services:
            return self.services[service_name]

        if not self.creds_path:
            msg = (
                "Không tìm thấy file xác thực trong Credentials/! "
                "Vui lòng đảm bảo file Credentials/google_workspace_credentials.json tồn tại."
            )
            log_action("auth", "FAILED", msg)
            raise FileNotFoundError(msg)

        try:
            from google.oauth2 import service_account
            from google.oauth2.credentials import Credentials
            from google_auth_oauthlib.flow import InstalledAppFlow
            from googleapiclient.discovery import build

            scopes = [
                'https://www.googleapis.com/auth/gmail.readonly',
                'https://www.googleapis.com/auth/gmail.send',
                'https://www.googleapis.com/auth/calendar',
                'https://www.googleapis.com/auth/drive',
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/documents'
            ]

            with open(self.creds_path, 'r', encoding='utf-8') as f:
                cred_data = json.load(f)

            creds = None
            if cred_data.get("type") == "service_account":
                creds = service_account.Credentials.from_service_account_file(
                    self.creds_path, scopes=scopes
                )
            else:
                token_path = os.path.join(CREDENTIALS_DIR, "token.json")
                if os.path.exists(token_path):
                    creds = Credentials.from_authorized_user_file(token_path, scopes)

                if not creds or not creds.valid:
                    if creds and creds.expired and creds.refresh_token:
                        from google.auth.transport.requests import Request
                        creds.refresh(Request())
                    else:
                        print("🔐 Đang tạo link xác thực tài khoản Google...", flush=True)
                        flow = InstalledAppFlow.from_client_secrets_file(
                            self.creds_path, scopes=scopes
                        )
                        auth_url, _ = flow.authorization_url(prompt='consent')
                        print(f"\n👉 LINK XÁC THỰC GOOGLE: {auth_url}\n", flush=True)
                        creds = flow.run_local_server(port=0, open_browser=True)

                    with open(token_path, 'w', encoding='utf-8') as token_file:
                        token_file.write(creds.to_json())
                    print("✅ Xác thực thành công! Đã lưu token.json.")

            service = build(service_name, version, credentials=creds)
            self.services[service_name] = service
            return service

        except ImportError:
            msg = "Thiếu thư viện Google Client library! Vui lòng cài đặt: pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib"
            log_action("dependency_check", "FAILED", msg)
            print(msg)
            sys.exit(1)

    # 📧 GMAIL METHODS
    def list_emails(self, query="maxResults=10", max_results=10):
        """Liệt kê danh sách mail từ Gmail."""
        try:
            service = self._get_service('gmail', 'v1')
            results = service.users().messages().list(userId='me', maxResults=max_results, q=query).execute()
            messages = results.get('messages', [])
            email_list = []
            
            for msg in messages:
                detail = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
                headers = detail.get('payload', {}).get('headers', [])
                
                subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '(Không tiêu đề)')
                sender = next((h['value'] for h in headers if h['name'].lower() == 'from'), '(Không rõ)')
                date = next((h['value'] for h in headers if h['name'].lower() == 'date'), '')
                snippet = detail.get('snippet', '')
                
                email_list.append({
                    'id': msg['id'],
                    'from': sender,
                    'subject': subject,
                    'date': date,
                    'snippet': snippet
                })

            log_action("gmail_list", "SUCCESS", {"count": len(email_list)})
            return email_list
        except Exception as e:
            log_action("gmail_list", "ERROR", {"error": str(e)})
            raise

    def send_email(self, to, subject, body, is_html=False):
        """Gửi Email qua Gmail API."""
        try:
            import base64
            from email.mime.text import MIMEText

            service = self._get_service('gmail', 'v1')
            message = MIMEText(body, 'html' if is_html else 'plain')
            message['to'] = to
            message['subject'] = subject
            
            raw_msg = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
            res = service.users().messages().send(userId='me', body={'raw': raw_msg}).execute()
            
            log_action("gmail_send", "SUCCESS", {"to": to, "subject": subject, "id": res.get("id")})
            return res
        except Exception as e:
            log_action("gmail_send", "ERROR", {"error": str(e)})
            raise

    # 📅 CALENDAR METHODS
    def create_calendar_event(self, summary, start_time, end_time, description="", location="", attendees=None):
        """Tạo cuộc họp / sự kiện trên Google Calendar."""
        try:
            service = self._get_service('calendar', 'v3')
            event = {
                'summary': summary,
                'location': location,
                'description': description,
                'start': {'dateTime': start_time, 'timeZone': 'Asia/Ho_Chi_Minh'},
                'end': {'dateTime': end_time, 'timeZone': 'Asia/Ho_Chi_Minh'},
                'attendees': [{'email': email} for email in (attendees or [])],
                'conferenceData': {
                    'createRequest': {'requestId': f"req_{int(datetime.now().timestamp())}", 'conferenceSolutionKey': {'type': 'hangoutsMeet'}}
                }
            }
            res = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()
            log_action("calendar_create", "SUCCESS", {"summary": summary, "htmlLink": res.get("htmlLink")})
            return res
        except Exception as e:
            log_action("calendar_create", "ERROR", {"error": str(e)})
            raise

    # 📁 DRIVE METHODS
    def search_drive(self, query):
        """Tìm kiếm file/thư mục trên Google Drive."""
        try:
            service = self._get_service('drive', 'v3')
            results = service.files().list(q=query, fields="files(id, name, mimeType, webViewLink)").execute()
            files = results.get('files', [])
            log_action("drive_search", "SUCCESS", {"query": query, "count": len(files)})
            return files
        except Exception as e:
            log_action("drive_search", "ERROR", {"error": str(e)})
            raise

    # 📊 SHEETS METHODS
    def read_sheet(self, spreadsheet_id, range_name):
        """Đọc dữ liệu từ Google Sheets."""
        try:
            service = self._get_service('sheets', 'v4')
            result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
            values = result.get('values', [])
            log_action("sheets_read", "SUCCESS", {"spreadsheet_id": spreadsheet_id, "rows": len(values)})
            return values
        except Exception as e:
            log_action("sheets_read", "ERROR", {"error": str(e)})
            raise

    def append_sheet_row(self, spreadsheet_id, range_name, values):
        """Thêm dòng mới vào Google Sheets."""
        try:
            service = self._get_service('sheets', 'v4')
            body = {'values': values}
            result = service.spreadsheets().values().append(
                spreadsheetId=spreadsheet_id, range=range_name,
                valueInputOption="USER_ENTERED", body=body
            ).execute()
            log_action("sheets_append", "SUCCESS", {"spreadsheet_id": spreadsheet_id, "updates": result.get("updates")})
            return result
        except Exception as e:
            log_action("sheets_append", "ERROR", {"error": str(e)})
            raise

    # 📝 DOCS METHODS
    def create_document(self, title, content=""):
        """Tạo tài liệu Google Docs mới."""
        try:
            service_docs = self._get_service('docs', 'v1')
            doc = service_docs.documents().create(body={'title': title}).execute()
            doc_id = doc.get('documentId')

            if content:
                requests = [{'insertText': {'location': {'index': 1}, 'text': content}}]
                service_docs.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()

            log_action("docs_create", "SUCCESS", {"title": title, "documentId": doc_id})
            return doc
        except Exception as e:
            log_action("docs_create", "ERROR", {"error": str(e)})
            raise

def main():
    parser = argparse.ArgumentParser(description="Google Workspace CLI Helper for AI Agent")
    subparsers = parser.add_subparsers(dest="service", help="Các dịch vụ: gmail, calendar, drive, sheets, docs")

    # Gmail parser
    gmail_parser = subparsers.add_parser("gmail")
    gmail_parser.add_argument("action", choices=["send", "list"])
    gmail_parser.add_argument("--to", help="Người nhận email")
    gmail_parser.add_argument("--subject", help="Tiêu đề email")
    gmail_parser.add_argument("--body", help="Nội dung email")
    gmail_parser.add_argument("--query", default="", help="Query tìm kiếm mail (ví dụ: 'is:unread')")
    gmail_parser.add_argument("--max", type=int, default=10, help="Số lượng mail tối đa")

    # Calendar parser
    cal_parser = subparsers.add_parser("calendar")
    cal_parser.add_argument("action", choices=["create"])
    cal_parser.add_argument("--summary", required=True)
    cal_parser.add_argument("--start", required=True)
    cal_parser.add_argument("--end", required=True)
    cal_parser.add_argument("--desc", default="")

    # Drive parser
    drive_parser = subparsers.add_parser("drive")
    drive_parser.add_argument("action", choices=["search"])
    drive_parser.add_argument("--query", required=True)

    # Sheets parser
    sheets_parser = subparsers.add_parser("sheets")
    sheets_parser.add_argument("action", choices=["read", "append"])
    sheets_parser.add_argument("--id", required=True)
    sheets_parser.add_argument("--range", required=True)
    sheets_parser.add_argument("--values", help="JSON array array string: '[[\"a\", \"b\"]]'")

    # Docs parser
    docs_parser = subparsers.add_parser("docs")
    docs_parser.add_argument("action", choices=["create"])
    docs_parser.add_argument("--title", required=True)
    docs_parser.add_argument("--content", default="")

    args = parser.parse_args()

    if not args.service:
        parser.print_help()
        sys.exit(0)

    client = GoogleWorkspaceClient()

    if args.service == "gmail":
        if args.action == "list":
            emails = client.list_emails(query=args.query, max_results=args.max)
            print(f"\n📫 ĐÃ TÌM THẤY {len(emails)} EMAIL MỚI/LIÊN QUAN:\n" + "="*50)
            for i, email in enumerate(emails, 1):
                print(f"[{i}] Từ: {email['from']}")
                print(f"    Tiêu đề: {email['subject']}")
                print(f"    Ngày: {email['date']}")
                print(f"    Tóm tắt: {email['snippet']}\n" + "-"*50)
        elif args.action == "send":
            res = client.send_email(args.to, args.subject, args.body)
            print(f"✅ Gửi email thành công ID: {res.get('id')}")

    elif args.service == "calendar" and args.action == "create":
        res = client.create_calendar_event(args.summary, args.start, args.end, description=args.desc)
        print(f"✅ Tạo lịch hẹn thành công: {res.get('htmlLink')}")

    elif args.service == "drive" and args.action == "search":
        files = client.search_drive(args.query)
        print(f"🔍 Tìm thấy {len(files)} tệp:")
        for f in files:
            print(f" - {f['name']} (ID: {f['id']}) - Link: {f.get('webViewLink')}")

    elif args.service == "sheets":
        if args.action == "read":
            rows = client.read_sheet(args.id, args.range)
            print(f"📊 Kết quả đọc {len(rows)} dòng:")
            for r in rows:
                print(r)
        elif args.action == "append":
            vals = json.loads(args.values)
            res = client.append_sheet_row(args.id, args.range, vals)
            print(f"✅ Đã thêm dữ liệu vào Sheet thành công!")

    elif args.service == "docs" and args.action == "create":
        res = client.create_document(args.title, args.content)
        print(f"✅ Tạo Google Doc thành công ID: {res.get('documentId')}")

if __name__ == "__main__":
    main()
