


# def trainee_register(request):
#     username = form.cleaned_data.get("username")
#     email = form.cleaned_data.get("email")
#     ######################### mail system ####################################
#     htmly = get_template("email.html")
#     d = {"username": username}
#     subject, from_email, to = (
#         "welcome to Fitness",
#         settings.EMAIL_HOST_USER,
#         email,
#     )
#     html_content = htmly.render(d)
#     msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
#     msg.attach_alternative(html_content, "text/html")
#     try:
#         msg.send()
#     except:
#         # TODO - create 404 pages
#         print("email not working")
#         pass
#     ##################################################################
#     messages.success(
#         request, f"Your account has been created! You are now able to log in"
#     )


def trainer_register(request):
    # TrainerRegisterForm
    if request.method == "POST":
        # TODO - update trainer information
        pass
    else:
        form = UserRegisterForm()
        trainer_form = TrainerRegisterForm()

    return render(request, "trainer_register.html", {"form": form, "trainer_form": trainer_form})
