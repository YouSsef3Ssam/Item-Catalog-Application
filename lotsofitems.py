from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *


# Create database and create a shortcut
engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create user
User1 = User(name="Youssef", email="youssef@itemcatalog.com")
session.add(User1)
session.commit()

# Create category of Soccer
category1 = Categories(user_id=1, name="Soccer")
session.add(category1)
session.commit()

# Create Items For Soccer


SoccerItem1 = CategoryItem(name="Goal Keeping Gloves", user_id=1,
                           description="Gloves provides a better grip",
                           categories=category1)
session.add(SoccerItem1)
session.commit()

SoccerItem2 = CategoryItem(name="Soccer cleats", user_id=1,
                           description="Soccer Cleats are made of rubber",
                           categories=category1)
session.add(SoccerItem2)
session.commit()

SoccerItem3 = CategoryItem(name="Shin Guards", user_id=1,
                           description="Provides protection to player shins",
                           categories=category1)
session.add(SoccerItem3)
session.commit()

SoccerItem4 = CategoryItem(name="Socks", user_id=1,
                           description="Socks are usually knee length",
                           categories=category1)
session.add(SoccerItem4)
session.commit()

SoccerItem5 = CategoryItem(name="Shorts", user_id=1,
                           description="Soccer shorts are  above the knee",
                           categories=category1)
session.add(SoccerItem5)
session.commit()


# Create category of Basketball
category2 = Categories(user_id=1, name="Basketball")
session.add(category2)
session.commit()

# Create Items For Basketball
BasketballItem1 = CategoryItem(name="Basketball Bat", user_id=1,
                               description="The Basketball Arbitral Tribunal"
                               "(BAT) is an independent body, officially"
                               "recognised by FIBA and outlined by the FIBA"
                               "General Statutes, providing services for"
                               "the rapid and simple resolution of disputes"
                               "between players, agents, coaches and clubs"
                               "through arbitration. It was established in"
                               "2006 (as the FIBA Arbitral Tribunal).",
                               categories=category2)
session.add(BasketballItem1)
session.commit()


# Create category of Baseball
category3 = Categories(user_id=1, name="Baseball")
session.add(category3)
session.commit()

# Create Items For Baseball
BaseballItem1 = CategoryItem(name="Baseball Bat", user_id=1,
                             description="baseball to hit the ball after it is"
                             "thrown by the pitcher. By regulation it may be "
                             "no more than 2.75 inches (70 mm) in diameter at"
                             "the thickest part and no more than 42 inches"
                             "(1,100 mm) long.", categories=category3)
session.add(BaseballItem1)
session.commit()


# Create category of Fribee
category4 = Categories(user_id=1, name="Fribee")
session.add(category4)
session.commit()

# Create Items For Fribee
FribeeItem1 = CategoryItem(name="Fribee", user_id=1,
                           description="a game played on a rectangular field"
                           "between two seven-player teams in which a plastic"
                           "disc is advanced by being thrown from player to"
                           "player and in which a team scores by catching"
                           "a throw in the opponent's end zone",
                           categories=category4)
session.add(FribeeItem1)
session.commit()


# Create category of Snowboarding
category5 = Categories(user_id=1, name="Snowboarding")
session.add(category5)
session.commit()

# Create Items For Snowboarding
SnowboardingItem1 = CategoryItem(name="Snowboarding", user_id=1,
                                 description="Snowboarding is a recreational"
                                 "activity and Olympic and Paralympic sport"
                                 "that involves descending a snow-covered"
                                 "slope while standing on a snowboard attached"
                                 "to a rider's feet.", categories=category5)
session.add(SnowboardingItem1)
session.commit()


# Create category Rock Climbing
category6 = Categories(user_id=1, name="Rock Climbing")
session.add(category6)
session.commit()

# Create Items For Climbing
ClimbingItem1 = CategoryItem(name="Climbing Mountains", user_id=1,
                             description="Mountain climbing (or mountaineer"
                             "ing)"
                             "is a hobby where people climb mountains.[2] It "
                             "may involve hiking, , rock climbing, as well as"
                             "crossing glaciers. Someone who does mountain"
                             "climbing is called a mountain climber.",
                             categories=category6)
session.add(ClimbingItem1)
session.commit()


# Create category of Foosball
category7 = Categories(user_id=1, name="Foosball")
session.add(category7)
session.commit()

# Create Items For Foosball
FoosballItem1 = CategoryItem(name="Foosball", user_id=1,
                             description="Table football or table soccer,"
                             "foosball in North America, is a table-top game"
                             "that is loosely based on football.[1] The aim of"
                             "the game is to use the control knobs to move the"
                             "ball into the opponent’s goal. There are no"
                             "unified rules for playing the game, in the sense"
                             "that rules vary in different countries and even"
                             " in"
                             "cities, and sometimes between different clubs in"
                             "the same city.", categories=category7)
session.add(FoosballItem1)
session.commit()


# Create category of Skating
category8 = Categories(user_id=1, name="Skating")
session.add(category8)
session.commit()

# Create Items For Skating
SkatingItem1 = CategoryItem(name="Shorts", user_id=1,
                            description="Skating involves any sports or"
                            "recreational activity which consists of traveling"
                            "on surfaces or on ice using skates.There are"
                            "several different kinds of skating",
                            categories=category8)
session.add(SkatingItem1)
session.commit()


# Create category of Hockey
category9 = Categories(user_id=1, name="Hockey")
session.add(category9)
session.commit()

# Create Items For Hockey
HockeyItem1 = CategoryItem(name="Hockey", user_id=1,
                           description="Ice Hockey is a contact team sport"
                           "played on ice, usually in a rink, in which two"
                           "teams of skaters use their sticks to shoot a"
                           "vulcanized rubber puck into their opponent's"
                           "net to score points", categories=category9)
session.add(HockeyItem1)
session.commit()

print ("Done!")
