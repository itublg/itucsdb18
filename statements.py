import sources from data

NEW_STATEMENTS = {
    "createUserTable" :
        """CREATE TABLE IF NOT EXISTS public.users (
                username varchar(50) NOT NULL,
                userpassword char(32) NOT NULL,
                email varchar(50) NOT NULL,
                profile_image INT default 0,
                gold int NOT NULL DEFAULT 0,
                score int NOT NULL DEFAULT 0,
                CONSTRAINT users_pk PRIMARY KEY (username),
                isAdmin bool default false
        )""",
    "createFriendsTable" :
        """CREATE TABLE IF NOT EXISTS public.friends (
                username varchar(50) NOT NULL,
                friend varchar(50) NOT NULL,
                FOREIGN KEY (username) REFERENCES public.users(username)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (friend) REFERENCES public.users(username)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                CONSTRAINT friends_pk PRIMARY KEY (username,friend)
        )""",
    "createFriendRequestsTable" :
        """CREATE TABLE IF NOT EXISTS public.friendrequests (
                sender varchar(50) NOT NULL,
                friend varchar(50) NOT NULL,
                CONSTRAINT friendrequests_pk PRIMARY KEY (sender,friend),
                FOREIGN KEY (sender) REFERENCES public.users(username)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (friend) REFERENCES public.users(username)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
        )""",
    "createMessagesTable":
        """CREATE TABLE if not EXISTS Messages(
        message_id serial primary key,
        sender varchar(50) not null,
        receiver varchar(50) not null,
        message varchar(255),
        FOREIGN KEY (sender) REFERENCES public.users(username)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        FOREIGN KEY (receiver) REFERENCES public.users(username)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        )
        """,
    "createSourceTypesTable" :
        """CREATE TABLE IF NOT EXISTS public.sourcetypes (
                stype varchar(50) NOT NULL,
                CONSTRAINT sourcetypes_pk PRIMARY KEY (stype)
        )""",
    "createCitiesTable" :
        """CREATE TABLE IF NOT EXISTS public.cities (
                cityname varchar(50) NOT NULL,
                username varchar(50) NOT NULL,
                xcoordiante bigint NOT NULL,
                ycoordiante bigint NOT NULL,
                buildinglimit bigint NOT NULL,
                buildingcount bigint NOT NULL,
                CONSTRAINT cities_pk PRIMARY KEY (cityname),
                FOREIGN KEY (username) REFERENCES public.users(username)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
        )""",
    "createSourcesTable" :
        """CREATE TABLE IF NOT EXISTS public.sources (
                username varchar(50) NOT NULL,
                stype varchar(50) NOT NULL,
                count bigint NOT NULL,

                CONSTRAINT sources_pk PRIMARY KEY (username,stype),
                FOREIGN KEY (username) REFERENCES public.users(username) 
                    ON DELETE CASCADE 
                    ON UPDATE CASCADE,
                FOREIGN KEY (stype) REFERENCES public.sourcetypes(stype)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
        )""",
    "createBaseProductionsTable" :
        """CREATE TABLE IF NOT EXISTS public.baseproductions (
                cityname varchar(50) NOT NULL,
                stype varchar(50) NOT NULL,
                baseproduction bigint NOT NULL,
                CONSTRAINT baseproductions_pk PRIMARY KEY (cityname,stype),
                FOREIGN KEY (cityname) REFERENCES public.cities(cityname)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (stype) REFERENCES public.sourcetypes(stype)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
        )""",
    "createBaseLimitsTable" :
        """CREATE TABLE IF NOT EXISTS public.baselimits (
                username varchar(50) NOT NULL,
                stype varchar(50) NOT NULL,
                baselimit bigint NOT NULL,
                CONSTRAINT baselimits_pk PRIMARY KEY (username,stype),
                FOREIGN KEY (username) REFERENCES public.users(username) 
                    ON DELETE CASCADE 
                    ON UPDATE CASCADE,
                FOREIGN KEY (stype) REFERENCES public.sourcetypes(stype)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
        )""",
    "createProductionsTable" :
        """CREATE TABLE IF NOT EXISTS public.productions (
                cityname varchar(50) NOT NULL,
                stype varchar(50) NOT NULL,
                production bigint NOT NULL,
                CONSTRAINT productions_pk PRIMARY KEY (cityname,stype),
                FOREIGN KEY (cityname) REFERENCES public.cities(cityname)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (stype) REFERENCES public.sourcetypes(stype)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
        )""",
    "createLimitsTable" :
        """CREATE TABLE IF NOT EXISTS public.limits (
                username varchar(50) NOT NULL,
                stype varchar(50) NOT NULL,
                sourcelimit bigint NOT NULL,
                CONSTRAINT limits_pk PRIMARY KEY (username,stype),
                FOREIGN KEY (username) REFERENCES public.users(username) 
                    ON DELETE CASCADE 
                    ON UPDATE CASCADE,
                FOREIGN KEY (stype) REFERENCES public.sourcetypes(stype)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
        )""",
    "createEffectTypesTable" :
        """CREATE TABLE IF NOT EXISTS public.effecttypes (
                etype varchar(50) NOT NULL,
                CONSTRAINT effecttypes_pk PRIMARY KEY (etype)
        )""",
    "createBuildingTypesTable" :
        """CREATE TABLE IF NOT EXISTS public.buildingtypes (
                buildingname varchar(50) NOT NULL,
                buildtime bigint NOT NULL,
                CONSTRAINT buildingtypes_pk PRIMARY KEY (buildingname)
        )""",
    "createBuildingEffectsTable" :
        """CREATE TABLE IF NOT EXISTS public.buildingeffects (
                buildingname varchar(50) NOT NULL,
                stype varchar(50) NOT NULL,
                etype varchar(50) NOT NULL,
                value bigint NOT NULL,
                CONSTRAINT buildingeffects_pk PRIMARY KEY (buildingname,stype,etype),
                FOREIGN KEY (buildingname) REFERENCES public.buildingtypes(buildingname)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (stype) REFERENCES public.sourcetypes(stype)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (etype) REFERENCES public.effecttypes(etype)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
        )""",
    "createBuildingCostsTable" :
        """CREATE TABLE IF NOT EXISTS public.buildingcosts (
                buildingname varchar(50) NOT NULL,
                costsource varchar(50) NOT NULL,
                cost bigint NOT NULL,
                CONSTRAINT buildingcosts_pk PRIMARY KEY (buildingname,costsource),
                FOREIGN KEY (buildingname) REFERENCES public.buildingtypes(buildingname)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (costsource) REFERENCES public.sourcetypes(stype)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
        )""",
}

INIT_STATEMENTS_ORDER = [
    "createUserTable",
    "createFriendsTable",
    "createFriendRequestsTable",
    "createMessagesTable",
    "createSourceTypesTable",
    "createCitiesTable",
    "createSourcesTable",
    "createBaseProductionsTable",
    "createBaseLimitsTable",
    "createProductionsTable",
    "createLimitsTable",
    "createEffectTypesTable",
    "createBuildingTypesTable",
    "createBuildingEffectsTable",
    "createBuildingCostsTable",
]

def insert_user(cursor,username, password, email):
    cursor.execute("""
    INSERT INTO users VALUES(
    %s,
    %s,
    %s
    )
    """,(username, password, email))


def insert_city(cursor,city_major, city_name, city_location):
    cursor.execute("""
    INSERT INTO CITY VALUES(
    %s,
    %s,
    %s
    )
    """,(city_major, city_name, city_location))


def friend_request(cursor, sender, receiver):
    cursor.execute("""insert into friendrequests
                    (sender, friend) values
                    (%s, %s)""", (sender, receiver))


def insert_friend(cursor, user1, user2):
    cursor.execute(
    """DELETE FROM public.friendrequests
            WHERE sender=%s AND friend=%s""",(user2, user1)
    )
    cursor.execute(
    """insert into friends
            (username, friend) values (%s, %s)""", (user1, user2))

    cursor.execute(
    """insert into friends
            (username, friend) values (%s, %s)""", (user2, user1))


def your_message(cursor, sender, receiver, message):
    cursor.execute("""INSERT INTO Messages (message_id, sender, receiver, message) VALUES (DEFAULT, %s, %s, %s);""",(sender, receiver, message))

def delete_message(cursor, id):
    cursor.execute("""
    DELETE FROM MESSAGES WHERE messages.id=id
    """)

def delete_friend(cursor, username, friend):
    cursor.execute("""select username,friend from friends where(username=%s and friend=%s)""",(username, friend))
    if cursor.fetchone() is None:
        Print("Friend delete no friend")
        return False
    cursor.execute("""delete from friends where (username=%s and friend=%s)""",(username, friend))
    cursor.execute(""" delete from friends where(username=%s and friend=%s)""",(friend, username))
    return True


def accept_friend(cursor, sender, friend): # sender = session['username'], friend = username
    cursor.execute("""select count(*) from public.friendrequests
                    WHERE sender=%s AND friend=%s""", (sender, friend))
    if cursor.fetchone() is None:
        return 0 #return render_template('logged.html', error="error") #no such request
    cursor.execute("""
                    select username from friends where(username=%s and friend=%s)
                    """,(sender,friend))
    if cursor.fetchone() is None:
         return 1 #They are not friends before
    else:
        cursor.execute("""DELETE FROM public.friendrequests
                    WHERE sender=%s AND friend=%s""",(friend, sender))
        return 2


def reject_friend(cursor, sender, friend):
    cursor.execute("""
    DELETE FROM public.friendrequests WHERE sender=%s AND friend=%s
    """,(friend, sender))


#def new_building(cursor, buildingName):
#yeni bina building tablesine 0 olarak eklenecek
#pending building tablesina level 1 olarak eklenecek
#bina masraflari dusulecek kullanicidan

#def levelup_building(cursor, buildingis):
#buildings tablesinde leveli x olan bina pending building tablesine x+1 olarak eklenecek
#bina yukselme masraflari kullanicidan dusulecek

def tupleList2List(tupleList):
    normalList = []
    for (i,) in tupleList:
        normalList.append(i)
    return normalList

def get_all_usernames(cursor):
    cursor.execute("""select username from public.users""")
    return tupleList2List(cursor.fetchall())

def get_all_cities(cursor):
    cursor.execute("""select cityname from public.cities""")
    return tupleList2List(cursor.fetchall())

def get_cities_of_user(cursor, username):
    cursor.execute("""select cityname from public.cities
                        where username=%s""", (username,))
    return tupleList2List(cursor.fetchall())

def get_user_source_limits(cursor, username):
    cursor.execute("""select stype,value from public.limits
                        where username=%s""", (username,))

    limitsUser = cursor.fetchall()
    limitsDict = { }
    for s in sources:
        limitsDict[s] = 0


    for (stype, value) in limitsUser:
        limitsDict[stype] += value

    return limitsDict


def update_all_sources(cursor):
    cities = get_all_cities(cursor)
    for city in cities:
        city_production = get_production_of_city(city)
        username = get_user_of_city(city)
        sources = get_sources_of_user(username)
        for key in city_production:
            sources[key] +=city_production[key]
        
        limits = get_user_source_limits(cursor, username)

        update_user_sources(cursor, username, sources, limits)         


def get_sources_of_user(cursor, username):
    cursor.execute("""select stype,value from public.sources
                        where username=%s""", (username,))

    sourcesUser = cursor.fetchall()
    sourcesDict = { }
    for s in sources:
        sourcesDict[s] = 0


    for (stype, value) in sourcesUser:
        sourcesDict[stype] += value

    return sourcesDict


#return building ids
def get_buildings_of_city(cursor, cityname):
    cursor.execute("""select buildingid from public.buildings
                        where cityname=%s""", (cityname,))
    return tupleList2List(cursor.fetchall())

def get_baseproductions_of_city(cursor, city):
    cursor.execute("""select stype, value from public.baseproductions
                        where cityname=%s""", (cityname,))
    baseproductions = cursor.fetchall()
    baseproductionsDict = { }

    for (stype, value) in productions:
        baseproductionsDict[stype] = value

    return baseproductionsDict

def get_base_building_productions(cursor, buildingname):
    cursor.execute("""select stype, value from public.baseproductions
                        where buildingname=%s and etype='inc'""", (buildingname,))
    baseproductions = cursor.fetchall()
    baseproductionsDict = { }

    for (stype, value) in productions:
        baseproductionsDict[stype] = value

    return baseproductionsDict

def get_base_building_factors(cursor, buildingname):
    cursor.execute("""select stype, value from public.baseproductions
                        where buildingname=%s and etype='factor'""", (buildingname,))
    basefactors = cursor.fetchall()
    basefactordict = { }

    for (stype, value) in basefactors:
        basefactordict[stype] = value

    return basefactordict

def get_buildingname(cursor, buildingid):
    cursor.execute("""select buildingname from public.buildings
                        where buildingid=%s""", (buildingid,))

    (buildingname,) = cursor.fetchone()
    return buildingname

def get_building_level(cursor, buildingid):
    cursor.execute("""select level from public.buildings
                        where buildingid=%s""", (buildingid,))

    (level,) = cursor.fetchone()
    return level


LEVEL_EFFECT = 10 #percent
def get_building_productions(cursor, buildingid):
    level = get_building_level(cursor, buildingid)
    effect = level * LEVEL_EFFECT
    productions = get_base_building_productions(cursor, buildingid)

    for key in productions:
        productions[key] += (productions[key] * effect) // 100

    return productions

LEVEL_EFFECT = 10 #percent
def get_building_factors(cursor, buildingid):
    level = get_building_level(cursor, buildingid)
    effect = level * LEVEL_EFFECT
    factors = get_base_building_productions(cursor, buildingid)

    for key in factors:
        factors[key] += (factors[key] * effect) // 100

    return factors



def get_production_of_city(cursor, cityname):

    productions = get_baseproductions_of_city(cityname)

    factors = {}

    buildings = get_buildings_of_city(cursor, cityname)

    for building in buildings:
        prods = get_building_productions(cursor, building)
        for prod in prods:
            productions[prod] += prods[prod]
        #endfor

        facts = get_base_building_factors(cursor, building)

        for fac in facts:
            factors[fac] += facts[fac]
        #endfor

    #endfor

    for key in productions:
        productions[key] +=  (factors[key] * productions[key]) // 100

    return productions


def change_city_major(cursor, username, cityname):
    cursor.execute("""
    UPDATE public.cities
    SET  username=%s
    WHERE(cityname=%s)
    """, (username, cityname))
    cursor.commit()


def get_user_of_city(cursor, cityname):
    cursor.execute("""
    SELECT username FROM public.cities WHERE(cityname=%s)
    """, (cityname))
    user = cursor.fetchone()
    return user[0]


def update_user_sources(cursor, username, sources, limit):
    for key, values in sources:
        value = min(limit[key], values)
        cursor.execute("""
        UPDATE sources
        SET count=%s
        WHERE (username=%s)
        """,(value, username))
    cursor.commit()
