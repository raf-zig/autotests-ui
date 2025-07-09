import pytest

from playwright.sync_api import expect, Page
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
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

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(
        chromium_page_with_state: Page,
        create_course_page: CreateCoursePage,
        courses_list_page: CoursesListPage
):
    chromium_page_with_state.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title="",description="",estimated_time="",max_score="0",min_score="0")
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )











