from ..userModel import UserModel


def get_domain_email_ratio(domain: str) -> float:
    """Get the proportion of users who have an email address registered in a
    specific domain (for example, "example.com").

    :param domain: The domain that is used to find users with the same domain in email.
    :return: Percentage of users who have the same domain out of all users (Precision two decimal places).
    """
    total_users = UserModel.query.count()
    domain_users = UserModel.query.filter(UserModel.email.like(f"%@{domain}")).count()
    if total_users == 0:
        return 0.0
    else:
        return round((domain_users / total_users) * 100, 2)
