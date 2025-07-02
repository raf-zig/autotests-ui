from playwright.sync_api import expect, Page

def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    course_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(course_title).to_be_visible()
    expect(course_title).to_have_text("Courses")

    results_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(results_icon).to_be_visible()

    results_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(results_title).to_be_visible()
    expect(results_title).to_have_text("There is no results")

    results_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_text).to_be_visible()
    expect(results_text).to_have_text("Results from the load test pipeline will be displayed here")
