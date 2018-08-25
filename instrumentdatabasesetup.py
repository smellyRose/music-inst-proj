# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, MusicalInstrument, Model


engine = create_engine('sqlite:///instrumentmodels.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Bob Grass", email="bob_grass@rocketmail.com")
session.add(User1)
session.commit()

# Musical Instrument Guitar
MusicalInstrument1 = MusicalInstrument(user_id=1, name="Guitar", availableColors="Red,White,Black,Sunburst,Blue,Green,Natural")

session.add(MusicalInstrument1)
session.commit()

model1 = Model(user_id=1, name="Gibson 2016 Les Paul Studio HP Electric Guitar", description="The 2016 Les Paul Studio HP is the supercharged counterpart of the traditional Les Paul Studio, and introduces an advanced set of premium, high-performance features to the format, including a new and exclusive fast-access heel, developed specifically for the Gibson USA High Performance lineup, to allow unprecedented access to the high notes - which, combined with the new soloist neck width, provides the fastest and most comfortable Les Paul Studio neck you’ve ever played.",
                     price="$1,659.00", color="Sunburst", musicalInstrument=MusicalInstrument1)

session.add(model1)
session.commit()

model2 = Model(user_id=1, name="Fender American Professional Stratocaster Maple Fingerboard Electric Guitar", description="Often copied, but never surpassed, the Stratocaster is arguably the world’s most-loved electric guitar. Electrifying the music world since its debut in 1954, its natural, versatile sound made the Stratocaster the benchmark for exceptional guitar tones. The American Professional Stratocaster isn’t a re-imagining of the classic design; it’s the authentic original model, evolved.The choice of musical legends since its release, the Stratocaster feel and sound set the world on fire, powering music movements from electric blues to EDM, and everything in-between. In your hands this Strat is ready to navigate the creative twists and turns of your music, inspiring you to express yourself in new ways through your playingDeveloped by pickup master Tim Shaw, the brand-new V-Mod single-coil pickups are voiced specifically for each position, mixing alnico magnet types to produce powerful, nuanced tones with original Fender sonic DNA. Retain high-end clarity when adjusting the volume controls, thanks to the new treble-bleed tone circuit that lets your tone shine through in all its glory. The new modern “Deep C”-shaped neck profile feels just right in your hand while the narrow-tall frets make it easy to bend strings accurately and play perfectly intonated chords.The best of yesterday and today, the American Professional Stratocaster is the latest form of electric inspiration from Fender. Step up and stake your claim to a legend.",
                     price="$1,399.99", color="Red", musicalInstrument=MusicalInstrument1)

session.add(model2)
session.commit()

model3 = Model(user_id=1, name="Ibanez AZ2402 Prestige Electric Guitar", description="For 2018, Ibanez is introducing a new line of solid body electric guitars called the AZ series. Within that line, we are excited to announce the release of the AZ2402. Even though Ibanez tends to be a guitar brand associated with modern designs, we have decades of accumulated knowledge and a history to draw from, so pushing boundaries is nothing new for us.The AZ series carries with it all of the hallmarks of these tried and tested Ibanez qualities: the smooth oval neck profile, the well balanced asymmetrical body shape, and the neck heel allowing unrivaled playability an upper fret access. It also features a new tremolo bridge, as well as newly developed Hyperion pickups, produced in collaboration with Seymour Duncan. All of these elements help the AZ push the existing boundaries of playability and sound to the next level for modern cutting-edge players, while also providing a touch of classic styling.A first in guitar neck construction, The AZ’s neck is manufactured with S-TECH WOOD treated Maple. This nitrogen-heating-treatment increases the wood’s stability, durability, water resistance and tolerance of temperature changes. The neck is sealed with an oil finish (sealer coat) which helps make it feel similar to a well-played guitar neck. In order to achieve a supremely comfortable neck, the fretboard edge is finished with a smooth curve that extends through the border between the fretboard and the neck to the fretboard itself. The Oval C neck shape allows for a comfortable grip in the lower register, and a more modern feel in the higher register. Luminescent side dots also provide a great point of reference on dark stages. A shallow rear body contour combines with a larger forearm contour increases player comfort. The pickups, designed in collaboration with Seymour Duncan, are a moderate output pickup, sporting Alnico-5 magnets to keep the clarity of the fundamental tone while using distortion. This design also provides a dynamic and clear pick attack. From treble to bass, the overall tone is evenly balanced and works well with various effects. A newly developed dyna-MIX 10 switching system provides excellent versatility in that it has 10 different possible pickup combinations by way of the mini toggle and 5-way blade switch.  The T1802 bridge is a result of direct collaboration between Ibanez and GOTOH. It features machined titanium saddles and a solid steel tremolo block for a quick response and improved articulation. The narrower string spacing allows for easy picking across strings, for styles such as string skipping and hybrid picking. The snap and hold tremolo arm socket makes it easy to load a tremolo arm, and the arm torque adjuster allows for fine torque adjustments without any tools. The stud lock screws lock the stud bolts in place, for better tuning stability and resonance. The 2-point floating tremolo system creates a super smooth tremolo motion in either direction.  The AZ is also equipped with GOTOH H.A.P-M locking machine heads, which have an established reputation for tuning stability. Its H. A. P (Height Adjustable Post) system allows for the adjustment of string posts to attain appropriate tension on each individual string. Hardshell case included. ",
                     price="$1,999.99", color="Natural", musicalInstrument=MusicalInstrument1)

session.add(model3)
session.commit()

# Musical Instrument Bass
MusicalInstrument2 = MusicalInstrument(user_id=2, name="Bass", availableColors="Red,White,Black,Blue,Green")

session.add(MusicalInstrument2)
session.commit()

model1 = Model(user_id=2, name="Fender Special Edition Deluxe PJ Bass", description="We've teamed up with Fender to bring you another great-sounding, unique one-off bass loaded with premium features. The exclusive Deluxe PJ Bass has a Precision Bass body with the neck of a '70s Jazz Bass. It features the appointments you've come to love about most Fender instruments like an alder body, urethane finish, maple fingerboard and a Fender high mass bass bridge. Perhaps the most interesting feature aside from the mash-up of P Bass body and J Bass neck is the combination of Precision and Jazz Bass pickups. With this combo you get the best of both worlds. The growl of the passive J Bass bridge pickup blends perfectly with the passive P Bass split single coil neck pickup with the help of the volume and tone controls.",
                     price="$799.99", color="White", musicalInstrument=MusicalInstrument2)

session.add(model1)
session.commit()

model2 = Model(user_id=2, name="Rickenbacker 4003S Electric Bass Guitar", description="This traditional Rickenbacker bass style with dot inlays and no binding was prized by Paul McCartney and Chris Squire when they got their first 4001S models in 1964. Players cherish its traditional look and rounded edges that many claim make it more comfortable than the 4003.The updated 4003S version comes with the improved dual trussrod system. Of course, the famous solid bass tones, ringing sustain and treble punch we'e known for make it a dream. It' no wonder we™ve received a steady demand of requests to bring this back.This design was once exclusive to the British distributor Rose Morris in the sixties. Iconic curves of maple form the body with a traditional Rosewood fingerboard. Dot inlays and no binding make this stand out from the standard 4003.",
                     price="$1,715.12", color="Red", musicalInstrument=MusicalInstrument2)

session.add(model2)
session.commit()

model3 = Model(user_id=2, name="Rogue VB100 Violin Bass Guitar Vintage", description="A classic design with updated appointments to make it even sweeter than the original!The Rogue VB-100 violin bass guitar features a flamed maple arched top and back with the European-style hollowbody that makes it lightweight and capable of deep, resonant bass tones. The violin bass's traditional 31 inch scale offers immediate familiarity in your hands. A custom trapeze tailpiece, pearloid pickguard, and body binding on front and back are added touches. Don't be fooled by the tiny price; this Rogue a serious violin bass nicely made with all the playability and tone of the original at a fraction of the cost.",
                     price="$169.99", color="Blue", musicalInstrument=MusicalInstrument2)

session.add(model3)
session.commit()

# Musical Instrument Drums
MusicalInstrument3 = MusicalInstrument(user_id=3, name="Drums", availableColors="Blue Sparkle,Red Sparkle,Black")

session.add(MusicalInstrument3)
session.commit()

model1 = Model(user_id=1, name="DW Performance Series 5-Piece Shell Pack", description="With a look that is decidedly DW and a tone to match, the Performance Series exemplifies DW's commitment to handcrafted drums and value. The foundation of this kit, advanced HVX shells, were conceived, designed and constructed by John Good and the DW Custom Shop team in their Oxnard, California shell shop. The 8-ply HVX shells of this configuration (10-ply snare and kick shells) combine advanced grain orientation technology and hand-selected North American hard rock maple to deliver a low, punchy tone, with lush resonance and projection that's perfectly suited for live applications. Back-cut 45-degree bearing edges reduce shell-to-head contact to increase attack, while Suspension Tom Mounts (STM) collaborate to ensure a longer fundatmental tone. This Performance Series 5-piece kit is framed by chrome hardware and features classic DW quarter turret lugs and low mass die-cast claw hooks. It is available in a variety of finishes like satin oil, specialty lacquer and FinishPly„¢.",
                     price="$2,429.95 ", color="Blue Sparkle", musicalInstrument=MusicalInstrument3)

session.add(model1)
session.commit()

model2 = Model(user_id=1, name="Pearl Export Double Bass 8-Piece Drum Set", description="Like a legendary group or solo act whose mystique only grew during inactivity, the Export Series from Pearl is back and ready to help you take your act on the road. Unlike that aged group or musician, Pearl Export has only improved with age. Offering new hardware features, SST shell construction and suspended mounts, these Export drums are better than you remember them. The 6-ply poplar and mahogany shells churn out balanced attack and full tone, while the high-end hardware will make your trip down memory lane a pleasant one. Pearl's updated Export Series offers a sonically advanced recipe of strategically arranged plies of premium wood to maximize frequency response of every component. As with all Pearl drums, each shell is formed from our legendary SST construction process that uses extreme heat, Precision-cut scarf joints, proprietary Acoustiglue and over 1000lb. of hydraulic pressure to create the ultimate acoustic air chamber. Further emphasizing Pearl's sound first philosophy are the new lugs specifically designed for Export with sound-enhancement in mind. Designed for minimal shell interaction, they have a small footprint and low-mass for maximum resonance and sustain. Their bold look is modern but with a nod to lugs from Pearl's past. Export rack toms are equipped with Pearl's new Opti-Loc Mounting System that features a triangular design with two tension rod attachment points and another through one of the drum's two air vents. Rubber isolators at all connection points allow the drums to vibrate freely for maximum sustain and resonance while providing absolute and wobble-free performance.",
                     price="$1,159.00", color="Red Sparkle", musicalInstrument=MusicalInstrument3)

session.add(model2)
session.commit()

model3 = Model(user_id=1, name="TAMA Superstar Classic Custom 7-Piece Shell Pack", description="Superstar performance with the classic tones of maple. For nearly forty years the Superstar name has stood for groundbreaking design, superior build quality, sterling tone, and clear projection. Now Tama introduces this legendary kit in its most sonically aggressive persona yet...featuring 100% maple shells. Thinner and livelier than ever, the Tama designers have dialed in the perfect combination of sensitivity and high-end cut. Drawing on Superstar of the past, its classic Tama T-shape badge and streamlined low-mass single lugs point to the simpler state of art of the '70s, while the ingenious ­Star-Mount system eclipses everything in its class-all at a surprisingly affordable price.",
                     price="$899.99", color="Black", musicalInstrument=MusicalInstrument3)

session.add(model3)
session.commit()                   

# Musical Instrument Saxophone
MusicalInstrument4 = MusicalInstrument(user_id=4, name="Alto Saxophone", availableColors="Brass,White,Gold")

session.add(MusicalInstrument4)
session.commit()

model1 = Model(user_id=3, name="Etude EAS-100 Student Alto Saxophone Lacquer", description="Made out of fine metals for superior tone production, the Etude EAS-100 is the perfect instrument for starting out on the alto saxophone. The keywork, pads, and adjustment all work together to make tone production easier, more consistent, and stronger. And the bell brace and construction help make it as durable as possible. Includes case, mouthpiece, cap, and ligature. It may be tempting to buy a better horn used, but saxophones are mechanically complex, and if the horn is not well regulated and set up properly, it will be extremely difficult for a student to play. It is perhaps advisable then for a new student to get an Etude EAS-100, brand new, set up perfectly, and ready to play right out of the case. It will be shiny and beautiful, and your young saxophonist will jump up and down and squeal when he or she sees it. Pride of ownership inspires practice, and practice leads to success. Etude believes believe that price should not be a barrier to experiencing the growth and joy that comes from making music. That's why Etude offers you five of the most popular woodwind and brass instruments at an incredible price: flute, clarinet, alto sax, trumpet, and trombone. And no matter which you choose, you get a great design and outstanding construction that will give you years of musical enjoyment. See for yourself!",
                     price="$799.99", color="Brass", musicalInstrument=MusicalInstrument4)

session.add(model1)
session.commit()

model2 = Model(user_id=3, name="Allora Paris Series Professional Alto Saxophone", description="Precise intonation, quick response, and a big sound are just a few of the great features you will find in the Allora Paris Series Saxophones. The attention to detail, from the hand-engraving to the key adjustment is usually reserved for instruments that are much more expensive. You truly cannot go wrong with this alto saxophone. Featuring ribbed construction, a red brass body, Pisoni Pro pads, hand engraving, and a choice of finishes, the Paris Series Alto Saxophone is as fun to play as it is good looking. Every Allora instrument undergoes a shop key adjustment usually reserved for instruments that are much more expensive. You truly cannot go wrong with this fine alto.",
                     price="$1,499.99", color="Gold", musicalInstrument=MusicalInstrument4)

session.add(model2)
session.commit()

model3 = Model(user_id=3, name="Allora Vienna Series Intermediate Alto Saxophone", description="The Allora Vienna Series Intermediate Alto Saxophone gives sax players who want to step up a better instrument with reassuring key action, great looks, and the ability to perform just about any kind of music. Allora Vienna Series Saxophones are a great value for both student instrumentalists and school music programs on a budget. As affordable step-up instruments, Allora Vienna saxophones do an excellent job of combining features that enhance the sound with features that enhance durability. The result is that Allora Vienna saxophones provide years of service to a wide range of players. An Allora Vienna Series Intermediate Alto Saxophones could be just the solution you have been looking for.",
                     price="$1,099.99", color="Brass", musicalInstrument=MusicalInstrument4)

session.add(model3)
session.commit() 

# Musical Instrument Flute
MusicalInstrument5 = MusicalInstrument(user_id=5, name="Flute", availableColors="White,Silver,Gold")

session.add(MusicalInstrument5)
session.commit()

model1 = Model(user_id=4, name="Gemeinhardt 2SP Series Student Flute 2SP - Standard", description="Durably constructed for years of playability, the Gemeinhardt 2SP allows the beginning flutist to grow musically with every note he or she plays. Each Gemeinhardt 2SP student flute features a silver plated head, body and foot, plateau (closed hole) keys and a C foot. Complete with a strong plastic case and cleaning supplies, the Gemeinhardt 2SP is the ideal flute for the student or beginning adult flutist. This instrument is a legend in school band programs across the world. It satisfies the requirements of playability, sound quality and affordability that make a great student instrument. Very few other flutes rival it in these three categories. Tens of thousands of these flutes have found their way into the hands of students, many of whom have gone on to advanced playing. A fourth generation flutemaker, Kurt Gemeinhardt dedicated himself to creating remarkably responsive instruments with a beautiful tone which would distinguish them from all others. Today Gemeinhardt continues his legacy by crafting flutes that achieve a delicate balance between superb artistry and sophisticated technology for flutists of all talents and abilities.",
                     price="$479.00", color="White", musicalInstrument=MusicalInstrument5)

session.add(model1)
session.commit()

model2 = Model(user_id=4, name="The Etude EFL-100 flute is a quality instrument to fit any budget. It features a silver-plated head, body, and foot for beauty as well as durability. The C foot and offset-G key help make the instrument easier to hold and play for those with smaller hands. Etude believes that price should not be a barrier to experiencing the growth and joy that comes from making music. That's why Etude offers you five of the most popular woodwind and brass instruments at an incredible price: flute, clarinet, alto sax, trumpet, and trombone. And no matter which you choose, you get a great design and outstanding construction that will give you years of musical enjoyment. See for yourself.", description="2",
                     price="$269.99", color="White", musicalInstrument=MusicalInstrument5)

session.add(model2)
session.commit()

model3 = Model(user_id=4, name="Gemeinhardt 3SHB Series Intermediate Flute", description="The model 3SHB offers the resonance and tone quality of a solid silver headjoint combined with the French key mechanism (open-hole keys) often requested on an intermediate student instrument. The 3SHB offers specifications many teachers recommend for a step-up student flute.",
                     price="$999.00", color="Gold", musicalInstrument=MusicalInstrument5)

session.add(model3)
session.commit() 

# Musical Instrument Trombone       
MusicalInstrument6 = MusicalInstrument(user_id=6, name="Trombone", availableColors="Brass,White")

session.add(MusicalInstrument6)
session.commit()

model1 = Model(user_id=2, name="Etude ETB-100 Series Student Trombone Lacquer", description="The Etude ETB-100 Series Student Trombone features a .495 inch bore designed for easy tone production and projection. This trombone also features a brass outer handslide and crook plus a chrome inner handslide for enhanced durability. Includes a mouthpiece and case. The ETB-100 displays a great design and reflects Etude's commitment to outstanding construction, resulting in an instrument that will give you years of musical enjoyment and give your student every chance to develop a lifelong association with the love of music.",
                     price="$199.99", color="Brass", musicalInstrument=MusicalInstrument6)

session.add(model1)
session.commit()

model2 = Model(user_id=2, name="Allora AATB-202F Series Intermediate Trombone", description="The Allora AATB-202F trombone features a .547 inch large bore design with an open wrap F-attachment that offers less resistance and a full sound. This great-sounding instrument also comes with an 8.5 inch yellow brass bell for outstanding resonance plus a chrome inner and brass outer handslide for excellent action. Durable braces have a solid feel and ensure years of performance. Comes complete with a Cordura covered case and a large shank mouthpiece.",
                     price="$719.99", color="Brass", musicalInstrument=MusicalInstrument6)

session.add(model2)
session.commit()

model3 = Model(user_id=2, name="Allora ATBB-450 Vienna Series Bass Trombone Lacquer Yellow Brass Bell", description="The Allora ATBB-450 Vienna Series Bass Trombone is an affordable trombone for school programs or the advancing musician. The .562-inch bore offers a larger overall sound projected through the 9.5 inch yellow brass bell. Featuring a standard leadpipe, inline traditional rotor, open wrap F-attachment design along with the well weighted hand slide, the ATBB-450 is perfect for any school program or advancing musician. Comes complete with a premium nylon polyfoam case, a large shank mouthpiece and a three-year warranty. A used or extraordinarily cheap instrument can actually lessen your child’s likelihood of continuing in music. With the Allora Vienna series, you get a quality instrument that will play in tune, withstand student treatment, and inspire pride of ownership. ",
                     price="$2,499.99", color="Brass", musicalInstrument=MusicalInstrument6)

session.add(model3)
session.commit() 
