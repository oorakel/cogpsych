# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Shawn", color="#0080ff") # blue
define m = Character("Mum", color="#800080") # purple
define t = Character("Travel Influencer", color="#008000") # green

# The game starts here.

# Chapter 1
label start: # chapter 1
    scene bg room
    show shawn sg
    show mum sg at right
    with dissolve

    m "Shawn, what do you think of going to Japan at the end of next year?"

    show shawn smile
    with dissolve
    show mum sg
    with dissolve

    m "Haha, it's a good idea right?"
    m "I was thinking we could visit some areas in Hokkaido first before heading to Tokyo."
    m "But the problem is, I'm quite busy organising a seminar that my hotel is hosting…"
    m "I think your sister's also quite busy with her poly assignments and whatnot."
    m "I know you know quite a bit about Japan, and seeing how you're on holiday right now, could you help us plan our trip?"

    show shawn frown
    with dissolve
    show mum sg
    with dissolve

    s "Dang, I still can't get a break during the holidays…"
    m "!" # Glare (you can add a visual effect here if you want)
    s "B-but still!... It would be a pleasure to plan our trip!"

    # Scene 2
    scene bg room # Keep the room background
    show phone at center
    with dissolve
    t "Sapporo in Hokkaido – the go-to destination for every tourist and their grandma. You've got the rich, soul-warming miso ramen, the charming Odori Park for a nice wander, and of course, the spectacular ice sculptures at the winter festival. What's not to love?"
    t "But hold on – let's talk about Hakodate. This quiet little gem on Hokkaido's southern tip often gets overlooked, and frankly, it's criminal."
    t "Sure, it's a bit off the beaten path – fewer English-speaking hotels and the odd awkward hand-gesture conversation with the locals who likely don't speak a lick of English – but it more than makes up for it."
    t "Picture this: fresh-as-it-gets seafood at the Hakodate Morning Market, where you can even catch your own squid for sashimi. Then there's the star-shaped Goryokaku Fort, a slice of history wrapped in beautiful parkland that turns into a cherry blossom wonderland in spring. And let's not forget the view from Mount Hakodate, often called one of the top three night views in Japan – it's worth braving the cold for. Add in charming red-brick warehouses converted into trendy shops and cafes, and Hakodate's got everything for the adventurous traveller looking for a slower-paced, culturally rich escape."

    s "Let's see here, mum wants to head to Hokkaido first, but where?"
    s "This guy makes a really good point for Hakodate as a travel destination. My Japanese is at the level of a 6 year old though…"
    s "With Sapporo I know we'll definitely be able to communicate easier with people. But with Hakodate, it looks more fun but I'm not sure if they'll understand us enough for us to do anything.."

    menu:
        "Choose Sapporo - Seems fun and communication is definitely possible.":
            $ destination = "Sapporo"
        "Choose Hakodate - Seems more fun, but uncertain of whether communication is possible.":
            $ destination = "Hakodate"

    # Scene 3
    scene bg room
    show computer at center
    with dissolve

    s "Okay, let's see here…"
    s "I found 2 flights taking off from Singapore on the date that mum outlined"
    s "There's one flight from Scoot and another from Singapore airlines"
    s "Looking at the airlines price wise, Singapore airlines is more expensive but I know that we have an SQ membership with vouchers so that means that both flights are going to be approximately the same price"
    s "And at that time of the year, I also know that SQ has a tendency to overbook, with all of the Singaporeans going to Japan and whatnot."
    s "I can't be certain that my family can all guarantee seats even if we book it early."
    s "At the same time, I also know SQ's flights are going to be much better than Scoot comfort-wise."
    s "Hm……"

    menu:
        "Choose Singapore Airlines - Unconfirmed seating, but more comfort":
            $ airline = "Singapore Airlines"
        "Choose Scoot - Confirmed seating, but less comfort":
            $ airline = "Scoot"

    # Scene 4
    scene bg room
    show computer at center
    with dissolve

    s "Alrighty! That's the airline settled. Now onto what travel visa service we want to get."
    s "We have to get a visa either way to get into the country… That means I have to choose between these two companies and pay the cost for the visas. Hmmm, company A gives a guaranteed fast-track visa within 7 days for \$50, while company B has a way lower price of \$20! That's pretty neat. But it does say here that there's an 80\% chance of processing within 7 days and a 20\% chance of rejection…"
    s "Which one should I go for?"

    menu:
        "Company A - Higher price, but a confirmed Visa":
            $ visa = "Company A"
        "Company B - Lower price, but a high chance of getting a Visa":
            $ visa = "Company B"

    # Scene 5
    scene bg room
    show computer at center
    with dissolve

    s "Mum's really making me do all of the work, huh? Now I have to choose which travel insurance we should get for the trip."
    s "Starr Insurance's insurance plan ensures that I'll receive a guaranteed reimbursement of \$450 for expenses up to \$500 in case of an accident. On HL Assurance's website, it says that I only risk losing 10\% of expenses with their plan in case anything goes wrong. What should I do?"

    menu:
        "Starr Insurance - Receive a guaranteed reimbursement of \$450 for expenses up to \$500 in case of an accident":
            $ insurance = "Starr Insurance"
        "HL Assurance - Lose only 10\% of expenses in case of an accident":
            $ insurance = "HL Assurance"

    # Scene 6
    scene bg room
    show computer at center
    with dissolve

    s "Alright, last thing that I have to worry about. The transport."
    s "I have our transport route planned out approximately, and calculated the total cost of the tickets if we buy the tickets for each stop individually. It looks like all in all, if I do that, transport will cost \$41 per person for all 8 days in Hokkaido. Alternatively, I could buy the JR pass for \$276 per person for 7 days in Hokkaido."

    menu:
        "Buy tickets individually - \$41":
            $ transport = "Individual Tickets"
        "Buy the JR pass - \$276":
            $ transport = "JR Pass"

    # Scene 7
    scene bg room
    show mum sg at right
    with dissolve

    m "Shawn, about the travel insurance that you suggested."
    s "Yeah? What about it?"
    m "The insurance plans that you evaluated are from 2019, and I'm pretty sure that there have been changes made to the policies then, could help me take a look again?"
    s "Sure! I'll give the travel insurance another look."
    s "Let me see here… Starr Insurance's new policy states that with their plan, I will only face a potential loss of \$50 for expenses up to \$500 in case of an accident. HL Assurance's new policy states that I will receive an ensured reimbursal of 90\% of expenses in case of an accident. What should I go for?"

    menu:
        "Starr Insurance - Face a potential loss of \$50 for expenses up to \$500 in case of an accident.":
            $ insurance = "Starr Insurance Updated"
        "HL Assurance - Receive a guaranteed reimbursement of 90\% of expenses in case of an accident.":
            $ insurance = "HL Assurance Updated"

    s "And that's about all! Man, I'm glad I don't have to plan anymore."
    jump chapter_1
    return

    label chapter_1:
        hide mum with dissolve
        if destination == "Sapporo":
            "In terms of destination, you chose {b}Sapporo{/b}. We ended up going to Sapporo, but the high amount of tourist traps and crowded areas really dimmed down our experience. Despite the comfort of being surrounded by English we went home wondering what our trip would have been like if we went to Hakodate instead."
        else:
            "In terms of destination, you chose {b}Hakodate{/b}. Even though it was tough with the language barrier at first, we managed to work around it using google translate and we had a great time."

        "In real life, my Family ended up going to both Hakodate and Sapporo, splitting our 8 days clean down the middle. Although it was true that the locals spoke less English and that there was less accommodation for english-speakers in Hakodate, I’d say the unique cultural experiences and great food made me enjoy it way more than I did Sapporo and its crowded and bustling urban streets. If I was given the choice to choose one over the other, I’d say that Hakodate would be the better option to make."

        if airline == "Singapore Airlines":
            "In terms of airline, you chose {b}Singapore Airlines{/b}. Although we took a gamble booking SQ, it was certainly worth it. The increased comfort from the extra legroom and high quality cushions made the excruciating 8 hour flight barely tolerable. In real life, we ended up choosing SQ. Though, in reality, despite the increased comfort I also ended up not sleeping a wink because my mum kept leaning on me in her sleep. But even then, I don’t dare to think how much more of a nightmare the flight would have been if I was on Scoot instead of SQ. In-flight entertainment truly saved my butt."
        else:
            "In terms of airline, you chose {b}Scoot{/b}. The peace of mind that came with confirmed seats on Scoot certainly did not follow when we were crammed in a small area for 8-hours on a red eye flight. We ended up extremely jetlagged when we landed in Hokkaido, which really ate into our first real day in Japan. In real life, we ended up choosing SQ."

        if visa == "Company A":
            "In terms of Visa, you chose {b}Company A{/b}. With company A’s visa assuring that we all had our Visas within the week, we all rested easy. Even though we spent a bit more money on the travel visa, we were glad that it was already settled."
        else:
            "In terms of Visa, you chose {b}Company B{/b}. It was quite stressful waiting throughout the week waiting for the confirmation on whether we had been rejected or not. We ended up being rejected 2 times, making us spend \$60…\$10 more dollars than if we went with company A in the first place. We thought about what we could have used that extra \$10 per person on in the trip."

        # prospect theory analysis
        $ risk_averse_choices = 0
        if destination == "Sapporo":
            $ risk_averse_choices += 1
        if airline == "Scoot":
            $ risk_averse_choices += 1
        if visa == "Company B":
            $ risk_averse_choices += 1

        if risk_averse_choices >= 2:
            "All in all, you, the player, were more prone to making decisions that minimise risk in attaining gains and maximising risk to avoid losses, which may have led to less optimal outcomes in my Japan trip. The majority of decisions that you made are in line with prospect theory."
        else:
            "All in all, you, the player, made the optimal choices for most of the scenarios! Despite your good judgement and decision making, a lot of people may not have made the optimal choices because of a decision making framework that is based in prospect theory."

        "I’ll have a more in depth discussion of what prospect theory is in the next chapter of this game."

    return # important: Ends the chapter