import pytest
import allure
from allure_commons.types import Severity

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.COURSES) # Добавили feature
@allure.story(AllureStory.COURSES) # Добавили story
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self,courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.empty_view.check_visible(
            title='There is no results', description='Results from the load test pipeline will be displayed here')

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage):
        create_course_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar_view_component.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="",description="",estimated_time="",max_score="0",min_score="0")
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.exercises_empty_view.check_visible(
            title='There is no exercises', description='Click on "Create exercise" button to create new exercise')
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.click_create_exercise_button()
        create_course_page.create_exercise_form.check_visible(index=0, title='Exercise title', description='Exercise description')
        create_course_page.create_exercise_form.fill(index=0, title='title1', description='description1')
        create_course_page.create_course_toolbar_view_component.check_visible(is_create_course_disabled=False)
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage):
        create_course_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_form.check_visible(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )
        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.fill(
            title="Playwright2",
            estimated_time="3 weeks",
            description="Playwright2",
            max_score="101",
            min_score="11"
        )
        create_course_page.create_course_form.check_visible(
            title="Playwright2",
            estimated_time="3 weeks",
            description="Playwright2",
            max_score="101",
            min_score="11"
        )
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright2",
            max_score="101",
            min_score="11",
            estimated_time="3 weeks"
        )










