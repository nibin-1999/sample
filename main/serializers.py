from rest_framework import serializers
import phonenumbers


class CountrySerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()
    flag_url = serializers.SerializerMethodField()
    calling_code = serializers.SerializerMethodField()

    def get_flag_url(self, obj):
        # Uses a public flag API based on the country code
        return f"https://flagcdn.com/w160/{obj.code.lower()}.png"

    def get_calling_code(self, obj):
        try:
            # Uses phonenumbers to get the calling code for a country
            calling_code = phonenumbers.country_code_for_region(obj.code)
            return f"+{calling_code}"
        except phonenumbers.phonenumberutil.RegionCodeNotImplementedError:
            return ""
