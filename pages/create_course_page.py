from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_exercise_form = CreateCourseExerciseFormComponent(page)
        self.create_course_exercises_toolbar_view_component = CreateCourseExercisesToolbarViewComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_toolbar_view_component = CreateCourseToolbarViewComponent(page)




