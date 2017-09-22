from selenium import webdriver


def before_all(context):
    context.google_user = context.config.userdata.get("usuario")
    context.google_passwd = context.config.userdata.get("senha")
    print("vai começar a malandragem rsrs")
    context.driver = webdriver.Firefox(
            executable_path="/home/paulo/Documents/geckodriver")


def before_feature(context, feature):
    print(feature.filename)
    # if "bug" in feature.tags:
    #     feature.skip()


def after_feature(context, feature):
    print(feature.duration)


def after_all(context):
    print("vai terminar a sacanagem :(")
    context.driver.quit()


# def after_step(context, step):
    # import ipdb
    # ipdb.post_mortem(step.exc_traceback)
