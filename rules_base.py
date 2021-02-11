from mit_library.production import IF, AND, OR, NOT, THEN, DELETE

# Humanoid Species
HUMANOID_INTERMEDIATE_RULE = IF(
    AND(
        '(?x) has blood',
        "(?x) has 4 limbs",
        "(?x) has no specifics"
    ),
    THEN('(?x) is a humanoid')
)

# Insectoid Species
INSECTOID_INTERMEDIATE_RULE = IF(
    AND(
        '(?x) has hemolymph',
        "(?x) has 4 limbs",
        '(?x) has wings',
    ),
    THEN('(?x) is an insectoid')
)

# Slugoid species
SLUGOID_INTERMEDIATE_RULE = IF(
    AND(
        '(?x) has hemocyanin',
        '(?x) has 2 limbs',
        '(?x) has tail'
    ),
    THEN("(?x) is a slug")
)

# Loonies
LOONIES_RULE = IF(
    AND(
        "(?x) is a humanoid",
        "(?x) is bipedal",
        "(?x) has height small",
        "(?x) has skin color pale",
        "(?x) has hair color silver"
    ),
    THEN('(?x) is a loonie')
)

# Mandalorians
MANDALORIANS_RULE = IF(
    AND(
        "(?x) is a humanoid",
        "(?x) is bipedal",
        "(?x) has height medium",
        "(?x) has skin color unknown",
        "(?x) has beskar armour",
    ),
    THEN("(?x) is Mandalorian")
)

#Chisses
CHISSES_RULE = IF(
    AND(
        "(?x) is a humanoid",
        "(?x) is bipedal",
        "(?x) has height medium",
        "(?x) has skin color blue",
        "(?x) has red eyes"
    ),
    THEN("(?x) is Chiss")
)

# Geonosians
GEONOSIANS_RULE = IF(
    AND(
        "(?x) is an insectoid",
        "(?x) is bipedal",
        "(?x) has height medium",
        "(?x) has skin color orange",
        "(?x) has elongated face"
    ),
    THEN("(?x) is Geonosian")
)

#Culisettos
CULISETTOS_RULE = IF(
    AND(
        "(?x) is an insectoid",
        "(?x) is quadrupedal",
        "(?x) has height small",
        "(?x) has skin color pink",
        "(?x) is tube-mouthed",
    ),
    THEN("(?x) is Culisetto")
)

#Hutts
HUTTS_RULE = IF(
    AND(
        "(?x) is a slug",
        "(?x) is unipedal",
        "(?x) has height tall",
        OR(
            "(?x) has skin color blue",
            "(?x) has skin color gold",
            "(?x) has skin color green"
        ),
        "(?x) is large",
    ),
    THEN("(?x) is Hutt")
)

TOURISTS_RULES_DICT = {
    "intermediate_rules": {
        "HUMANOID_INTERMEDIATE_RULE": HUMANOID_INTERMEDIATE_RULE,
        "INSECTOID_INTERMEDIATE_RULE": INSECTOID_INTERMEDIATE_RULE,
        "SLUGOID_INTERMEDIATE_RULE": SLUGOID_INTERMEDIATE_RULE
    },
    "species_rules": {
        "LOONIES_RULE": LOONIES_RULE,
        "MANDALORIANS_RULE": MANDALORIANS_RULE,
        "CHISSES_RULE": CHISSES_RULE,
        "GEONOSIANS_RULE": GEONOSIANS_RULE,
        "HUTTS_RULE": HUTTS_RULE,
        "CULISETTOS_RULE": CULISETTOS_RULE
    }
}


TOURISTS_RULES_LIST = [
    HUMANOID_INTERMEDIATE_RULE,
    INSECTOID_INTERMEDIATE_RULE,
    SLUGOID_INTERMEDIATE_RULE,
    LOONIES_RULE,
    MANDALORIANS_RULE,
    CHISSES_RULE,
    GEONOSIANS_RULE,
    HUTTS_RULE,
    CULISETTOS_RULE
]
