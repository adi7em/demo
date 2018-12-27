WORKCLASS_CHOICES = (
        ('Private', 'PR'),
        ('Self-emp-not-inc', 'SN'),
        ('Self-emp-inc', 'SS'),
        ('Federal-gov', 'FG'),
        ('Local-gov', 'LG'),
        ('State-gov', 'SG',),
        ('Without-pay', 'WP'),
        ('Never-worked', 'NW')
    )


EDUCATION_CHOICES = (
        ('Bachelors', 'BC'),
        ('Some-College', 'SC'),
        ('11th', '11'),
        ('HS-grad', 'HS'),
        ('Prof-school', 'PF'),
        ('Assoc-acdm', 'AA'),
        ('Assoc-voc', 'AV'),
        ('9th', '9T'),
        ('7th-8th', '78'),
        ('12th', '12'),
        ('Masters', 'MA'),
        ('1st-4th', '14'),
        ('10th', '10'),
        ('Doctorate', 'DR'),
        ('5th-6th', '56'),
        ('Preschool', 'PS')
    )


STATUS_CHOICES = (
       ('Married-civ-spouse', 'MC'),
       ('Divorced', 'DV'),
       ('Never-married', 'NM'),
       ('Separated', 'SP'),
       ('Widowed', 'WD'),
       ('Married-spouse-absent', 'MA'),
       ('Married-AF-spouse', 'MF')
    )


OCCUPATION_CHOICES = (
        ('Tech-support', 'TS'),
        ('Craft-repair', 'CR'),
        ('Other-service', 'OS'),
        ('Sales', 'SL'),
        ('Exec-managerial', 'EM'),
        ('Prof-speciality', 'PF'),
        ('Handlers-cleaners', 'HC'),
        ('Machine-op-inspct', 'MI'),
        ('Adm-clerical', 'AC'),
        ('Farming-fishing', 'FF'),
        ('Transport-moving', 'TM'),
        ('Priv-house-serv', 'PH'),
        ('Protective-serv', 'PS'),
        ('Armed-Forces', 'AF')
    )


RELATIONSHIP_CHOICES = (
      ('Wife', 'W'),
      ('Own-child', 'C'),
      ('Husband', 'H'),
      ('Not-in-family', 'N'),
      ('Other-relative', 'O'),
      ('Unmarried', 'U')
    )

RACE_CHOICES = (
    ('White', 'W'),
    ('Asian-Pac-Islander', 'I'),
    ('Amer-Indian-Eskimo', 'E'),
    ('Other', 'O'),
    ('Black', 'B')
)


SEX_CHOICES = (
        ('Male', 'M'),
        ('Female', 'F')
    )