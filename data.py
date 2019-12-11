sources = [
    "wood",
    "stone",
    "food",
    "metal",
    "population",
]

effects = [
    "limit", #maximum limiliti # kadar artirir
    "factor", #artirimlar hesaplandiktan sonra uretimi # ile carpar
    "inc", #uretimi # kadar arttirir
]

buildings = [   
    {
        "buildingname": "field",
        "buildTime": 20,
        "costs": {
            "wood": 20,
            "stone": 20,
        },
        "effects": {
            "inc": {
                "food": 5,
            },
        },
    },
    {
        "buildingname": "depository",
        "buildTime": 66,
        "costs": {
            "wood": 30,
            "stone": 30,
            "metal": 10,
        },
        "effects": {
            "limit": {
                "wood": 400,
                "stone": 400,
                "metal": 400,
            },
        },
    },
    {
        "buildingname": "mill",
        "buildTime": 20,
        "costs": {
            "wood": 40,
            "stone": 20,
            "metal": 10,
        },
        "effects": {
            "factor": {
                "food" : 1.2,
            },
        },
    },
    {
        "buildingname": "experimental",
        "buildTime": 99,
        "costs": {
            "wood": 99,
            "stone": 99,
            "metal": 99,
            "food": 99,
        },
        "effects": {
            "factor": {
                "food" : 9,
                "metal" : 9,
                "stone" : 9,
                "wood" : 9,
            },
            "limit": {
                "food" : 9,
                "metal" : 9,
                "stone" : 9,
                "wood" : 9,
            },
            "inc": {
                "food" : 9,
                "metal" : 9,
                "stone" : 9,
                "wood" : 9,
            },
        },
    },

]




def dataCreaterAndUpdater(cursor):
    for source in sources:
        cursor.execute("""insert into sourceTypes(stype) values(%s) 
            ON CONFLICT ON CONSTRAINT sourceTypes_pk DO UPDATE SET stype = %s""", (source,source))

    for effect in effects:
        cursor.execute("""insert into effectTypes(etype) values(%s) 
            ON CONFLICT ON CONSTRAINT effectTypes_pk DO UPDATE SET etype = %s""", (effect,effect))

    for building in buildings:
        cursor.execute("""insert into buildingTypes(buildingName,buildTime) values(%s,%s)
            ON CONFLICT ON CONSTRAINT buildingTypes_pk DO UPDATE SET 
            buildingName = %s, buildTime = %s""", 
            (building["buildingname"], building["buildTime"],
            building["buildingname"], building["buildTime"]))

        for source in building["costs"]:
            cursor.execute("""insert into buildingCosts(buildingName,costsource,cost) 
                values(%s,%s,%s) ON CONFLICT ON CONSTRAINT buildingCosts_pk DO UPDATE
                SET buildingName = %s, costsource = %s, cost = %s""", 
                    (building["buildingname"], source, building["costs"][source], 
                    building["buildingname"], source, building["costs"][source]))
        
        for effect in building["effects"]:
            for source in building["effects"][effect]:
                cursor.execute("""insert into buildingEffects(buildingName,stype,etype,value) 
                values(%s,%s,%s,%s) ON CONFLICT ON CONSTRAINT buildingEffects_pk DO UPDATE
                SET buildingName = %s, stype = %s, etype = %s, value = %s""", 
                    (building["buildingname"], source, effect, building["effects"][effect][source],
                    building["buildingname"], source, effect, building["effects"][effect][source]))