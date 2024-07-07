from django.db import models

class User(models.Model):
    """
    User model to store user information.
    
    Attributes:
        username (str): The unique username for the user.
        email (str): The unique email address for the user.
        date_joined (datetime): The date and time when the user joined.
    """
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the User object.
        
        Returns:
            str: The username of the user.
        """
        return self.username

class Friend(models.Model):
    """
    Friend model to represent the friendship relationship between users.
    
    Attributes:
        user (User): The user who has a friend.
        friend (User): The user who is a friend of the user.
    """
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friend_of', on_delete=models.CASCADE)

    class Meta:
        """
        Meta class to define the unique constraint.
        
        Ensures that a user cannot be friends with the same person more than once.
        """
        unique_together = ('user', 'friend')

    def __str__(self):
        """
        Returns the string representation of the Friend object.
        
        Returns:
            str: A string indicating the friendship relationship.
        """
        return f'{self.user.username} is friends with {self.friend.username}'
