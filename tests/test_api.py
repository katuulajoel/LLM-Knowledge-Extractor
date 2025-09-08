import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.test_text = """
        Artificial intelligence is transforming industries across the globe. 
        From healthcare to finance, AI applications are making processes more efficient.
        While there are concerns about job displacement, many experts believe AI will 
        create more jobs than it eliminates in the long run.
        """
    
    def test_analyze_endpoint(self):
        response = self.client.post(
            "/analyze",
            json={"text": self.test_text}
        )
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        
        # Check response structure
        self.assertIn("summary", data)
        self.assertIn("metadata", data)
        self.assertIn("title", data["metadata"])
        self.assertIn("topics", data["metadata"])
        self.assertIn("sentiment", data["metadata"])
        self.assertIn("keywords", data["metadata"])
        
        # Check types
        self.assertIsInstance(data["summary"], str)
        self.assertIsInstance(data["metadata"]["title"], str)
        self.assertIsInstance(data["metadata"]["topics"], list)
        self.assertIn(data["metadata"]["sentiment"].lower(), ["positive", "neutral", "negative"])
        self.assertIsInstance(data["metadata"]["keywords"], list)
        self.assertLessEqual(len(data["metadata"]["keywords"]), 3)

if __name__ == "__main__":
    unittest.main()
