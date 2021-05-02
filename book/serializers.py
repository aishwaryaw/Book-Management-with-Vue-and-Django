from rest_framework import serializers
from .models import Book
import re

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.
    """
    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

# Book serializer for handling book models data as per the request
class BookSerializer(serializers.ModelSerializer):
    get_poster_image = serializers.SerializerMethodField()
    poster_image = Base64ImageField(
        required=False,
        allow_null=True,
        allow_empty_file=True,
        max_length=None, 
        use_url=True,
    )
    
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "description",
            "poster_image",
            "get_poster_image"
        )

    def get_poster_image(self,obj):
        return obj.get_poster_image()

    # Customizing the validation of title and author fields
    def validate_title(self,value):
        if not bool(re.match('[a-zA-Z0-9\s]+$', value)):
            raise serializers.ValidationError("Only alphabets, numbers and spaces are allowed")
       
        return value
    
    def validate_author(self,value):
        if not bool(re.match('[a-zA-Z\s]+$', value)):
            raise serializers.ValidationError("Only alphabets and spaces are allowed")
        return value
   




    
    
