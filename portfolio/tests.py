from django.test import TestCase
from django.urls import reverse

from .views import FEATURED_PROJECTS


class PortfolioViewsTests(TestCase):
    def test_home_renders_all_featured_projects_and_publication(self):
        response = self.client.get(reverse("portfolio:home"))
        self.assertEqual(response.status_code, 200)
        for project in FEATURED_PROJECTS:
            self.assertContains(response, project["title"])
        self.assertContains(response, "Investigating Extreme Precipitation")
        self.assertContains(response, "Graduate Research Assistant")
        self.assertContains(response, "Prerak Patel Portfolio")
        self.assertContains(response, "Simple, useful software for small businesses.")
        self.assertContains(response, "Understanding the stock market.")
        self.assertContains(response, "02 / Projects")
        self.assertNotContains(response, "Selected projects")
        self.assertContains(response, "https://mail.google.com/mail/?view=cm")
        self.assertContains(response, "patel.prerak2798@gmail.com")
        self.assertContains(response, "https://github.com/prerakpatel51")
        self.assertContains(
            response, "https://www.linkedin.com/in/prerakpatel51020021998"
        )
        self.assertNotContains(response, "mailto:")

    def test_each_case_study_is_available(self):
        for project in FEATURED_PROJECTS:
            response = self.client.get(
                reverse("portfolio:project_detail", args=[project["slug"]])
            )
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, project["title"])
            self.assertContains(response, "My contribution")
            self.assertContains(response, "Technical decisions")
            self.assertContains(response, "Evaluation strategy")
            self.assertContains(response, project["contributions"][0])

    def test_projects_follow_the_requested_portfolio_order(self):
        self.assertEqual(
            [project["slug"] for project in FEATURED_PROJECTS],
            [
                "pkcast",
                "cross-domain-xai",
                "applypilot-ai",
                "context-shift-xai",
                "satellite-segmentor",
                "rainfall-forecasting",
                "3d-satellite-vae",
            ],
        )
        self.assertEqual(
            [project["number"] for project in FEATURED_PROJECTS],
            ["01", "02", "03", "04", "05", "06", "07"],
        )

    def test_project_archive_contains_only_top_seven_repositories(self):
        response = self.client.get(reverse("portfolio:project_archive"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["all_projects"]), 7)
        self.assertEqual(len(FEATURED_PROJECTS), 7)
        self.assertContains(response, "3D Satellite Variational Autoencoder")
        self.assertNotContains(response, "Medical LLM RAG")

    def test_unknown_project_returns_404(self):
        response = self.client.get("/projects/not-a-project/")
        self.assertEqual(response.status_code, 404)
