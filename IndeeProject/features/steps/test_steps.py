from behave import given, when, then
from tests.utils.indeeUtility import indeeUtility
""""
    Step-Definition Class : All the Keyword called out in ./features/indee.feature has been defined here.
    Execution Starts from "environment.py" file where Pre-Post condition of browser creation has been defined.
    Business logic is defined in utility class : "./features/utiles/indeeUtility.py"
"""


@given('I navigate to Indee Tv')
def navigate_to_url(context):
    context.utility = indeeUtility(context.driver)
    url = "https://indeedemo-fyc.watch.indee.tv/"
    context.utility.navigate(url)


@when('I sign in using the access code "{code}"')
def sign_in(context, code):
    context.utility.signInToIndee(code)


@when('I navigate to the video section')
def navigate_to_video(context):
    context.utility.navigateToVideo()
    context.utility.switchToDetailsSection()
    context.utility.switchToVideoSection()


@when('I play the video for {seconds:d} seconds')
def play_video(context, seconds):
    context.utility.playPauseVideo(seconds)


@then('I resume the video')
def resume_video(context):
    context.utility.resumeVideo()


@then('I change the volume to {volume:d}%')
def change_volume(context, volume):
    context.utility.changeVolume(volume)


@then('I set the resolution to "{resolution}"')
def set_resolution(context, resolution):
    context.utility.changeResolution(resolution)


@then('I pause and exit the player')
def pause_exit_player(context):
    context.utility.pauseAndExitPlayer()


@then('I sign out')
def sign_out(context):
    context.utility.signOut()
