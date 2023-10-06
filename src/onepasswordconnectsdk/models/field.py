"""
    1Password Connect

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class Field:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'section': 'FieldSection',
        'type': 'str',
        'purpose': 'str',
        'label': 'str',
        'value': 'str',
        'generate': 'bool',
        'recipe': 'GeneratorRecipe',
        'entropy': 'float',
        'totp': 'str'
    }

    attribute_map = {
        'id': 'id',
        'section': 'section',
        'type': 'type',
        'purpose': 'purpose',
        'label': 'label',
        'value': 'value',
        'generate': 'generate',
        'recipe': 'recipe',
        'entropy': 'entropy',
        'totp': 'totp'
    }

    def __init__(self, id=None, section=None, type='STRING', purpose=None, label=None, value=None, generate=False, recipe=None, entropy=None, totp=None):  # noqa: E501
        self._id = None
        self._section = None
        self._type = None
        self._purpose = None
        self._label = None
        self._value = None
        self._generate = None
        self._recipe = None
        self._entropy = None
        self._totp = None
        self.discriminator = None

        self.id = id
        if section is not None:
            self.section = section
        if type is not None:
            self.type = type
        if purpose is not None:
            self.purpose = purpose
        if label is not None:
            self.label = label
        if value is not None:
            self.value = value
        if generate is not None:
            self.generate = generate
        if recipe is not None:
            self.recipe = recipe
        if entropy is not None:
            self.entropy = entropy
        if totp is not None:
            self.totp = totp

    @property
    def id(self):
        """Gets the id of this Field.  # noqa: E501


        :return: The id of this Field.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Field.


        :param id: The id of this Field.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def section(self):
        """Gets the section of this Field.  # noqa: E501


        :return: The section of this Field.  # noqa: E501
        :rtype: FieldSection
        """
        return self._section

    @section.setter
    def section(self, section):
        """Sets the section of this Field.


        :param section: The section of this Field.  # noqa: E501
        :type: FieldSection
        """

        self._section = section

    @property
    def type(self):
        """Gets the type of this Field.  # noqa: E501


        :return: The type of this Field.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Field.


        :param type: The type of this Field.  # noqa: E501
        :type: str
        """
        self._type = type

    @property
    def purpose(self):
        """Gets the purpose of this Field.  # noqa: E501

        Some item types, Login and Password, have fields used for autofill. This property indicates that purpose.  # noqa: E501

        :return: The purpose of this Field.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this Field.

        Some item types, Login and Password, have fields used for autofill. This property indicates that purpose.  # noqa: E501

        :param purpose: The purpose of this Field.  # noqa: E501
        :type: str
        """
        allowed_values = ["", "USERNAME", "PASSWORD", "NOTES"]  # noqa: E501
        if purpose not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `purpose` ({}), must be one of {}"  # noqa: E501
                .format(purpose, allowed_values)
            )

        self._purpose = purpose

    @property
    def label(self):
        """Gets the label of this Field.  # noqa: E501


        :return: The label of this Field.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Field.


        :param label: The label of this Field.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def value(self):
        """Gets the value of this Field.  # noqa: E501


        :return: The value of this Field.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Field.


        :param value: The value of this Field.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def generate(self):
        """Gets the generate of this Field.  # noqa: E501

        If value is not present then a new value should be generated for this field  # noqa: E501

        :return: The generate of this Field.  # noqa: E501
        :rtype: bool
        """
        return self._generate

    @generate.setter
    def generate(self, generate):
        """Sets the generate of this Field.

        If value is not present then a new value should be generated for this field  # noqa: E501

        :param generate: The generate of this Field.  # noqa: E501
        :type: bool
        """

        self._generate = generate

    @property
    def recipe(self):
        """Gets the recipe of this Field.  # noqa: E501


        :return: The recipe of this Field.  # noqa: E501
        :rtype: GeneratorRecipe
        """
        return self._recipe

    @recipe.setter
    def recipe(self, recipe):
        """Sets the recipe of this Field.


        :param recipe: The recipe of this Field.  # noqa: E501
        :type: GeneratorRecipe
        """

        self._recipe = recipe

    @property
    def entropy(self):
        """Gets the entropy of this Field.  # noqa: E501

        For fields with a purpose of `PASSWORD` this is the entropy of the value  # noqa: E501

        :return: The entropy of this Field.  # noqa: E501
        :rtype: float
        """
        return self._entropy

    @entropy.setter
    def entropy(self, entropy):
        """Sets the entropy of this Field.

        For fields with a purpose of `PASSWORD` this is the entropy of the value  # noqa: E501

        :param entropy: The entropy of this Field.  # noqa: E501
        :type: float
        """

        self._entropy = entropy
    
    @property
    def totp(self):
        """Gets the TOTP. # noqa: E501
        
        For fields of type 'OTP' this is the one-time password code # noqa: E501

        :return: The TOTP of the Field. # noqa: E501
        :rtype: str
        """
        return self._totp
    
    @totp.setter
    def totp(self, totp):
        """Sets the totp of this Field.

        For fields of type 'OTP' this is the one-time password code # noqa: E501

        :param totp: The TOTP of this Field.  # noqa: E501
        :type: str
        """

        self._totp = totp

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr in self.openapi_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Field):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Field):
            return True

        return self.to_dict() != other.to_dict()
