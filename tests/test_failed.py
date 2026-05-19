from pages.home_page import HomePage

def test_failed_home_page_validation(page):
    home = HomePage(page)

    # This assertion is intentionally wrong to make the test FAIL
    assert "wrongtext" in page.title()