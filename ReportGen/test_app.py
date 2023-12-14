"""_summary_
"""
from unittest import TestCase

# from flask import session
from ReportGen import app

app.config["TESTING"] = True

app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]


class ReportGenTests(TestCase):
    """integration tests for the app"""

    def test_report_download_status(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Daily summary report generated", html)

    # def test_redirection(self):
    #     with app.test_client() as client:
    #         resp = client.get("/redirect-me")

    #         self.assertEqual(resp.status_code, 302)
    #         self.assertEqual(resp.location, "http://localhost/")

    # def test_redirection_followed(self):
    #     with app.test_client() as client:
    #         resp = client.get("/redirect-me", follow_redirects=True)
    #         html = resp.get_data(as_text=True)

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn('redirected', html)

    def test_session_info(self):
        with app.test_client() as client:
            ## session info section to be added
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)

    def test_session_info_set(self):
        with app.test_client() as client:
            ## session info section to be added
            resp = client.get("/")

            self.assertEqual(resp.status_code, 200)
