define s = Character("Shawn", color="#0080ff") # blue
define m = Character("Mum", color="#800080") # purple
define t = Character("Travel Influencer", color="#008000") # green
define k = Character("Kahneman", color = "#b00000") # red
define tv = Character("Tversky", color = "#ffc800") # yellow

# backgrounds
image bg room = "chapter1/shawn-room.png"

# explanation thingy
image excel = "chapter1/transport-excel.png"
image insurance_1 = "chapter1/insurance-cp1.png"
image insurance_2 = "chapter1/insurance-cp2.png"
image airline_computer = "chapter1/airline-computer.png"
image influencer = "chapter1/influencer-phone.png"
image visa = "chapter1/visa-computer.png"

# character sprites
image shawn happy = "sprites/shawn/shawn-happy.png"
image shawn disappointed = "sprites/shawn/shawn-disappointed.png"
image shawn encouraging = "sprites/shawn/shawn-encouraging.png"
image shawn excited = "sprites/shawn/shawn-excited.png"
image shawn neutral = "sprites/shawn/shawn-neutral.png"
image shawn panicked = "sprites/shawn/shawn-panicked.png"
image shawn lookback = "sprites/shawn/shawn-lb.png"
image shawn shocked = "sprites/shawn/shawn-shocked.png"
image shawn inspired = "sprites/shawn/shawn-inspired.png"
image shawn confused = "sprites/shawn/shawn-confused.png"

image mum happy = "sprites/mum/mum-happy.png"
image mum angry = "sprites/mum/mum-angry.png"
image mum nervous = "sprites/mum/mum-nervous.png"
image mum neutral = "sprites/mum/mum-neutral.png"

# The game starts here.

# Chapter 1
label start: # chapter 1
    $ is_prospect_1 = False
    play music "chapter1/music/scene1.mp3" fadein 1.0
    s "My trip to Japan... Where do I even begin?"
    s "If I remember correctly, it took place in 2023."
    s "My mom wanted to reward me for finishing my O-levels and finally graduating from secondary school."
    s "Let me think back to how everything started…"

    scene bg room
    "November, 2022"
    show shawn neutral
    show mum neutral at left
    with dissolve

    m "Shawn, what do you think of going to Japan at the end of next year?"

    show shawn excited
    with dissolve
    show mum happy
    with dissolve

    m "Haha, it's a good idea right? It would be a nice reward for you completing your O-levels"
    m "I was thinking we could visit some areas in Hokkaido first before heading to Tokyo."
    show mum nervous
    m "But the problem is, I'm quite busy organising a seminar that my hotel is hosting…"
    m "I think your sister's also quite busy with her poly assignments and whatnot."
    m "I know you know quite a bit about Japan, and seeing how you're on holiday right now, could you help us plan our trip?"

    show shawn disappointed
    with dissolve

    s "Dang, I still can't get a break during the holidays…"
    show mum angry
    m "!" # Glare (you can add a visual effect here if you want)
    show shawn panicked
    s "B-but still!... It would be a pleasure to plan our trip!"

    # Scene 2
    stop music fadeout 2.0
    play music "chapter1/music/scene2.mp3" fadein 2.0
    scene bg room # Keep the room background
    show influencer at center
    with dissolve
    t "Sapporo in Hokkaido – the go-to destination for every tourist and their grandma."
    t "You've got the rich, soul-warming miso ramen, the charming Odori Park for a nice wander, and of course, the spectacular ice sculptures at the winter festival. What's not to love?"
    t "But hold on – let's talk about Hakodate. This quiet little gem on Hokkaido's southern tip often gets overlooked, and frankly, it's criminal."
    t "Sure, it's a bit off the beaten path – fewer English-speaking hotels and the odd awkward hand-gesture conversation with the locals who likely don't speak a lick of English – but it more than makes up for it."
    t "Picture this: fresh-as-it-gets seafood at the Hakodate Morning Market, where you can even catch your own squid for sashimi."
    t "Then there's the star-shaped Goryokaku Fort, a slice of history wrapped in beautiful parkland that turns into a cherry blossom wonderland in spring."
    t "And let's not forget the view from Mount Hakodate, often called one of the top three night views in Japan – it's worth braving the cold for."
    t "Add in charming red-brick warehouses converted into trendy shops and cafes, and Hakodate's got everything for the adventurous traveller looking for a slower-paced, culturally rich escape."
    hide influencer
    show shawn neutral at right
    with dissolve
    s "Let's see here, mum wants to head to Hokkaido first, but where?"
    s "This guy makes a really good point for Hakodate as a travel destination. My Japanese is at the level of a 6 year old though..."
    s "With Sapporo I know we'll definitely be able to communicate easier with people. But with Hakodate, it looks more fun but I'm not sure if they'll understand us enough for us to do anything.."

    menu:
        "Choose Sapporo - Seems fun and communication is definitely possible.":
            $ destination = "Sapporo"
        "Choose Hakodate - Seems more fun, but uncertain of whether communication is possible.":
            $ destination = "Hakodate"

    # Scene 3
    stop music fadeout 2.0
    play music "chapter1/music/scene3.mp3" fadein 2.0
    scene bg room
    show airline_computer at center
    with dissolve

    s "Okay, let's see here..."
    s "I found 2 flights taking off from Singapore on the date that mum outlined."
    s "There's one flight from Scoot and another from Singapore airlines."
    s "Looking at the airlines price wise, Singapore airlines is more expensive but I know that we have an SQ membership with vouchers so that means that both flights are going to be approximately the same price."
    s "And at that time of the year, I also know that SQ has a tendency to overbook, with all of the Singaporeans going to Japan and whatnot."
    s "I can't be certain that my family can all guarantee seats even if we book it early."
    "(THESE STATEMENTS ARE NOT TRUE, BUT PLEASE PRETEND THAT THEY ARE)"
    s "At the same time, I also know SQ's flights are going to be much better than Scoot comfort-wise."
    s "Hm..."

    menu:
        "Choose Singapore Airlines - Unconfirmed seating, but more comfort":
            $ airline = "Singapore Airlines"
        "Choose Scoot - Confirmed seating, but less comfort":
            $ airline = "Scoot"

    # Scene 4
    stop music fadeout 2.0
    play music "chapter1/music/scene4.mp3" fadein 2.0
    scene bg room
    show visa at center
    with dissolve

    s "Alrighty! That's the airline settled. Now onto what travel visa service we want to get."
    "(Singaporeans don't need to apply for visas because of their passports but please pretend that this is true once again)"
    s "We have to get a visa either way to get into the country... That means I have to choose between these two companies and pay the cost for the visas."
    s "Hmmm, company A gives a guaranteed fast-track visa within 7 days for $50, while company B has a way lower price of $20! That's pretty neat. But it does say here that there's an 80\% chance of processing within 7 days and a 20\% chance of rejection..."
    s "Which one should I go for?"

    menu:
        "Company A - Higher price, but a confirmed Visa":
            $ visa = "Company A"
        "Company B - Lower price, but a high chance of getting a Visa":
            $ visa = "Company B"

    # Scene 5
    stop music fadeout 2.0
    play music "chapter1/music/scene5.mp3" fadein 2.0
    scene bg room
    show insurance_1 at center
    with dissolve

    s "Mum's really making me do all of the work, huh? Now I have to choose which travel insurance we should get for the trip."
    s "Starr Insurance's insurance plan ensures that I'll receive a guaranteed reimbursement of $450 for expenses up to $500 in case of an accident."
    s "On HL Assurance's website, it says that I only risk losing 10\% of expenses with their plan in case anything goes wrong. What should I do?"

    menu:
        "Starr Insurance - Receive a guaranteed reimbursement of $450 for expenses up to $500 in case of an accident":
            $ insurance = "Starr Insurance"
        "HL Assurance - Lose only 10\% of expenses in case of an accident":
            $ insurance = "HL Assurance"

    # Scene 6
    stop music fadeout 2.0
    play music "chapter1/music/scene1.mp3" fadein 2.0
    scene bg room
    show excel at center
    with dissolve

    s "Alright, last thing that I have to worry about. The transport."
    s "I have our transport route planned out approximately, and calculated the total cost of the tickets if we buy the tickets for each stop individually."
    s "It looks like all in all, if I do that, transport will cost $41 per person for all 8 days in Hokkaido. Alternatively, I could buy the JR pass for $276 per person for 7 days in Hokkaido."

    menu:
        "Buy tickets individually - $41":
            $ transport = "Individual Tickets"
        "Buy the JR pass - $276":
            $ transport = "JR Pass"

    # Scene 7
    stop music fadeout 2.0
    play music "chapter1/music/scene7.mp3" fadein 2.0
    scene bg room
    show mum neutral at left
    show shawn neutral at right
    with dissolve

    m "Shawn, about the travel insurance that you suggested."
    s "Yeah? What about it?"
    m "The insurance plans that you evaluated are from 2019, and I'm pretty sure that there have been changes made to the policies then, could help me take a look again?"
    hide shawn neutral
    show shawn happy at right
    s "Sure! I'll give the travel insurance another look."
    hide shawn happy
    show insurance_2 at center with dissolve
    s "Let me see here… Starr Insurance's new policy states that with their plan, I will only face a potential loss of $50 for expenses up to $500 in case of an accident."
    s "HL Assurance's new policy states that I will receive an ensured reimbursal of 90\% of expenses in case of an accident. What should I go for?"

    menu:
        "Starr Insurance - Face a potential loss of $50 for expenses up to $500 in case of an accident.":
            $ insurance = "Starr Insurance Updated"
        "HL Assurance - Receive a guaranteed reimbursement of 90\% of expenses in case of an accident.":
            $ insurance = "HL Assurance Updated"

    s "And that's about all! Man, I'm glad I don't have to plan anymore."
    jump chapter_1

image bg irl1 = "chapter1/endings/irl-1.png"
image bg irl2 = "chapter1/endings/irl-2.png"
image bg hakodate = "chapter1/endings/hakodate.png"
image bg sapporo = "chapter1/endings/sapporo.png"
image bg scoot = "chapter1/endings/scoot.png"
image bg sq = "chapter1/endings/sq.png"
image bg visaa = "chapter1/endings/visa-a.png"
image bg visab = "chapter1/endings/visa-b.png"

label chapter_1:
    hide mum 
    hide shawn
    with dissolve
    stop music fadeout 2.0
    play music "chapter1/music/scene8.mp3" fadein 2.0
    if destination == "Sapporo":
        show bg sapporo
        with dissolve
        "In terms of destination, you chose {b}Sapporo{/b}."
        "We ended up going to Sapporo, but the high amount of tourist traps and crowded areas really dimmed down our experience."
        "Despite the comfort of being surrounded by English we went home wondering what our trip would have been like if we went to Hakodate instead."
    else:
        show bg hakodate
        with dissolve
        "In terms of destination, you chose {b}Hakodate{/b}."
        "Even though it was tough with the language barrier at first, we managed to work around it using google translate and we had a great time."

    show bg irl2
    with dissolve
    "In real life, my Family ended up going to both Hakodate and Sapporo, splitting our 8 days clean down the middle."
    "Although it was true that the locals spoke less English and that there was less accommodation for english-speakers in Hakodate, I'd say the unique cultural experiences and great food made me enjoy it way more than I did Sapporo and its crowded and bustling urban streets."
    show bg irl1
    with dissolve
    "If I was given the choice to choose one over the other, I'd say that Hakodate would be the better option to make."

    if airline == "Singapore Airlines":
        show bg sq
        with dissolve
        "In terms of airline, you chose {b}Singapore Airlines{/b}."
        "Although we took a gamble booking SQ, it was certainly worth it. The increased comfort from the extra legroom and high quality cushions made the excruciating 8 hour flight barely tolerable."
        "In real life, we ended up choosing SQ. Though, in reality, despite the increased comfort I also ended up not sleeping a wink because my mum kept leaning on me in her sleep."
        "But even then, I don't dare to think how much more of a nightmare the flight would have been if I was on Scoot instead of SQ. In-flight entertainment truly saved my butt."
    else:
        show bg scoot
        with dissolve
        "In terms of airline, you chose {b}Scoot{/b}."
        "The peace of mind that came with confirmed seats on Scoot certainly did not follow when we were crammed in a small area for 8-hours on a red eye flight."
        "We ended up extremely jetlagged when we landed in Hokkaido, which really ate into our first real day in Japan. In real life, we ended up choosing SQ."
        "In real life, we ended up choosing SQ. Though, in reality, despite the increased comfort I also ended up not sleeping a wink because my mum kept leaning on me in her sleep."
        "But even then, I don't dare to think how much more of a nightmare the flight would have been if I was on Scoot instead of SQ. In-flight entertainment truly saved my butt."

    if visa == "Company A":
        show bg visaa
        with dissolve
        "In terms of Visa, you chose {b}Company A{/b}."
        "With company A's visa assuring that we all had our Visas within the week, we all rested easy. Even though we spent a bit more money on the travel visa, we were glad that it was already settled."
    else:
        show bg visab
        with dissolve
        "In terms of Visa, you chose {b}Company B{/b}."
        "It was quite stressful waiting throughout the week waiting for the confirmation on whether we had been rejected or not. We ended up being rejected 2 times, making us spend $60…$10 more dollars than if we went with company A in the first place."
        "We thought about what we could have used that extra $10 per person on in the trip."

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
        # is prospect theory
        $ is_prospect_1 = True
    else:
        "All in all, you, the player, made the optimal choices for most of the scenarios! Despite your good judgement and decision making, a lot of people may not have made the optimal choices because of a decision making framework that is based in prospect theory."

    "I'll have a more in depth discussion of what prospect theory is in the next chapter of this game."
    jump chapter_2

# background
image bg hall = "chapter2/hall.png"
# sprites
image kahneman neutral = "sprites/kahneman/kahn-neutral.png"
image kahneman thinking = "sprites/kahneman/kahn-think.png"
image kahneman explaining = "sprites/kahneman/kahn-explain.png"
image tversky neutral = "sprites/tversky/tver-neutral.png"
image tversky inviting = "sprites/tversky/tver-invite.png"
image tversky explaining = "sprites/tversky/tver-explain.png"

image prospectformula = "chapter2/prospectformula.png"
image sshaped = "chapter2/sshaped.jpg"
image weighingfunc = "chapter2/weighing.png"
image weighingfunc2 = "chapter2/weighing2.png"

label chapter_2:
    stop music fadeout 2.0
    play music "chapter2/music/scene1.mp3"
    scene bg hall # Replace with classroom background
    with fade

    "The year is 1979. The dominant theory in decision-making is {b}Utility Theory{/b}, which posits that people evaluate choices—called prospects—based on their usefulness and likelihood. But cracks in this theory are beginning to show, and two economists are on the brink of proposing something revolutionary."
    "You somehow find yourself in that very classroom where a breakthrough in Economic theory is about to happen. You overhear two prominent economics discussing the prevailing utility theory."
    
    show kahneman neutral at left # Replace with image
    show tversky neutral at right # Replace with image
    with dissolve

    k "So, Tversky, utility theory defines a prospect as a gamble, a choice with various outcomes and probabilities. "
    k "It's elegant, really—expected utility calculates a prospect's attractiveness by averaging each individual outcome's usefulness with its likelihood. Logical, isn't it?"
    tv "Logical, sure. But people aren't calculators, Kahneman. They have emotions, biases, quirks. Why else would someone prefer a guaranteed $100 over a 50\% chance at $250?" # Escaped %
    k "That is most certainly true!"
    k "You know, I've noticed recently that people disproportionately prefer outcomes that are certain when compared to probable outcomes, even when the probable outcome is rationally better using utility theory's method of calculating expected utility."
    hide kahneman
    hide tversky
    with dissolve
    "This was later dubbed the certainty effect."

    if destination == "Sapporo":
        scene bg sapporo
        with dissolve
        "Do you remember when you chose Sapporo for our travel destination? This choice reflects the certainty effect."
    else:
        scene bg hakodate
        with dissolve
        "Do you remember when you chose Hakodate for our travel destination? According to the prospect theory's certainty effect, most people would have chosen Sapporo." 
        "This is because Sapporo, despite seeming less fun than Hakodate, comes with the certainty of being able to do what we planned on doing because communication in Sapporo was certain."
        "Despite the fact that Hakodate could have provided a more fun experience, the certainty that Sapporo provided outweighed that outcome and hence made it more attractive according to the certainty effect."
    scene bg hall with fade
    show tversky explaining at right
    with dissolve
    tv "That is true Kahneman!"
    tv "Another thing I realised is that when I present the same options differently, people flip-flop their preferences."
    tv "They ignore shared elements and fixate on what's unique and different between the options, even if both choices have the same outcome framed differently! Haha!"
    hide Kahneman
    hide tversky
    with dissolve
    "This was later named the isolation effect."
    show insurance_1 with dissolve
    "Do you remember both times when you had to choose insurance? "
    "What if I were to tell you that Starr Insurance and HL Assurance's insurance plans were objectively identical both times? "
    "Starr Insurance reimburses $450 for expenses up to $500 dollars and HL assurance reimburses 90\% of expenses."
    show insurance_2 with dissolve
    "But framing one as minimising loss and the other as receiving reimbursement could lead to different preferences despite the fact that they were the same both times!" # Escaped %
    scene bg hall with fade
    show kahneman explaining at left with dissolve
    k "Have you also noticed that the certainty effect was inverted when it came to scenarios where both options involved losses?"
    tv "People disproportionately prefer choices where decreased losses were possible than choices with confirmed larger losses."
    "This was named the reflection effect."
    hide kahneman with dissolve
    if visa == "Company B":
        show bg visab with dissolve
        "Do you remember when you chose company B for the travel visa? This choice reflects the reflection effect."
    else:
        show bg visaa with dissolve
        "Do you remember when you chose company A for the travel visa?"
        "According to prospect theory's reflection effect, most people would have chosen company B. This is because there is going to be a definite loss in money in having to buy a travel visa to go overseas."
        "However, company B provided a possible lesser loss compared to company A's confirmed larger loss. The risk aversion from the certainty effect was flipped on its head to form an aversion to loss."
    scene bg hall with fade
    show tversky neutral at right with moveinright
    show kahneman neutral at left with moveinleft
    with dissolve
    "These three inconsistencies-certainty, isolation, and reflection-shaped the foundation of Kahneman and Tversky's revolutionary Prospect Theory.(Kahneman & Tversky, 1979)"
    "Tversky notices you, the player and invites you to join them."
    show tversky inviting with dissolve
    tv "Ah, a fellow decision-maker! You look like someone who has had to make a bunch of tough choices recently. Care to chat about how we make decisions?"
    jump prospect_theory_questions
    label prospect_theory_questions: # loop back here
        show tversky neutral at right
        show kahneman neutral at left
        menu:
            "What are the processes that take place in decision making according to prospect theory?":
                show tversky neutral at right with dissolve
                tv "Well, when we thought about it, Kahneman and I realised that there are 2 phases to decision making, the first of which is the editing phase."
                show kahneman explaining
                k "The editing phase simply refers to evaluating your options; grouping outcomes by their similarities, differences, setting a baseline (reference point) to define what is a loss and what is a gain."
                k "This is followed by a reframing of the options into more objective presentations to reduce biases caused by how choices are presented."
                show kahneman neutral #with dissolve
                show tversky inviting
                tv "Indeed. Following this stage, there's the evaluation phase, where individuals assign value to outcomes based on their usefulness and likelihood and decide on what choice to make." 
                show weighingfunc at Transform(size=(960, 540),xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
                tv "Kahneman and I noted that probabilities are often not weighted in a linear fashion, as low probabilities might be overestimated and moderate probabilities might be underestimated."
                hide weighingfunc with dissolve
                show sshaped at Transform(size=(960, 540),xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
                tv "In-line with the certainty effect and the reflection effect, we also noted that losses are weighted more heavily than gains; that is to say a loss hurts way more than an equivalent gain." 
                tv "After all of these values are accounted for, the individual will then make the decision with the highest subjective value."
                hide sshaped with dissolve
                jump prospect_theory_questions
            "Were there any issues with prospect theory?":
                show tversky explaining
                tv "Why yes, there were plenty, haha!" 
                tv "Our original function did not properly weigh rare events with extremely high impacts, underweighting them despite the fact that people still buy lottery tickets and fear plane crashes!"
                show tversky neutral
                show kahneman explaining
                show sshaped at Transform(size=(960, 540),xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
                k "Indeed, and our theory overemphasised on the “S-shaped” value function, the function that states that people dislike losses much more than they value equivalent gains."
                k "This led to scenarios where the model would point to making the objectively worse option, which does not follow stochastic dominance."
                k "Stochastic dominance is a basic rule of decision making that states that if one option is clearly better across all outcomes, it will be preferred."
                hide sshaped with dissolve
                show kahneman neutral #with dissolve
                hide tversky
                hide kahneman
                with dissolve
                show excel at center with dissolve
                "Do you remember when you were choosing the transport passes? Stochastic dominance states that most people would buy the tickets individually because it's way cheaper than buying the JR pass, even though both bring the same outcome."
                hide excel with dissolve
                show tversky neutral at right with dissolve
                show weighingfunc2 at Transform(size=(960, 540),xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
                tv "We solved this issue by altering our probability weighting function, giving a disproportionate attention to non-likely impactful events, reflecting how people in real life view them."
                hide weighingfunc2 with dissolve
                show kahneman thinking at left with dissolve
                k "We also began to calculate probabilities altogether instead of individually, avoiding violating stochastic dominance,"
                k "This allowed for our updated theory, called Cumulative Prospect Theory (Tversky & Kahneman, 1992) to be applied to a larger area of application."
                show tversky inviting #with dissolve
                tv "Previously, prospect theory could only be applied to risky prospects with a small number of outcomes, whereas cumulative prospect theory can be applied to both risky and uncertain prospects where probabilities may not be precisely known!"
                jump prospect_theory_questions
            "Are there any external influences on what guides our decisions with respect to prospect theory?":
                hide tversky
                hide kahneman
                with dissolve
                show shawn happy at right with dissolve
                with dissolve
                s "Well, yes! There have been multiple studies that used prospect theory as a base to see how certain influences can impact decision making."
                s "A study by Campos-Vazquez and Cuilty (2014) found that socio demographic characteristics affect rates of risk loss and aversion, but not the weighing probability function."
                s "They also found that a person's emotional state affects decision making, with sadness increasing risk aversion in gains and risk seeking in losses, amplifying the functions of prospect theory."
                show shawn neutral
                s "They also found that anger diminishes the impact of losses, reducing loss aversion significantly. But it was also found that anger does not impact risk aversion in gains in any way."
                show shawn happy
                s "Another study by Abdellaoui et al. (2011) found that even financial professionals behaved exactly according to prospect theory!" 
                show shawn neutral
                s "Though, with a little less loss aversion. One explanation for this decreased loss aversion is desensitisation due to experience and knowledge."
                show shawn panicked
                s "Even then, it's scary to think about how even professionals with years of experience are still subject to this little cognitive bias!"
                hide shawn with dissolve
                jump prospect_theory_questions
            "How can we reduce the influence of the effects of prospect theory in making decisions?":
                show kahneman explaining
                k "Well, with the isolation effect in mind, try visualising what each option entails, both similarities and differences."
                show tversky inviting
                tv "And with the influence of emotions on decision making, try to keep calm to minimise risk and loss aversions!"
                show kahneman thinking
                k "It would also be helpful to take a moment to think about the actual probabilities of each option, taking a moment to ask yourself if you're overestimating or underestimating their probability."
                jump prospect_theory_questions
            "That's all I have to ask, thank you!":
                jump chapter2_conclusion

label chapter2_conclusion:
    show kahneman explaining
    k "Utility Theory had its strengths, but we wanted to build something that reflects real-world behavior. Remember, understanding biases isn't about avoiding them entirely—it's about making better decisions despite them."
    hide kahneman
    hide tversky
    with dissolve
    show shawn encouraging at center with dissolve
    s "All in all, prospect theory boils down to avoiding risks when it comes to gains, preferring certainty and smaller gains over risk and larger gains..."
    s "and seeking risks when it comes to losses, preferring probable smaller losses over certain larger losses."
    show shawn happy
    s "While prospect theory as a heuristic is certainly helpful in helping us lighten our cognitive load and makes the optimal decisions most of the time..."
    s "Like Kahneman has said, as with most heuristics, there are times when it won't give you the best outcome possible."
    show shawn panicked
    s "(though the choices that people are more likely to make according to the effects outlined by prospect theory also won't be as exaggeratedly bad as shown in this game)"
    show shawn encouraging
    s "Understanding prospect theory will allow us to make better decisions despite these heuristics we have."
    show shawn happy zorder 10
    s "When it comes to things like vacation and travel, Studies by Van De Kaa (2010) and Lin et al. (2023) have shown that prospect theory actually does a better job of describing people's choices in travel and tourism than utility theory because of 3 main reasons:"
    s "Prospect theory's flexibility in describing different decision making strategies, prospect theory's inclusion of the different reference points that people have for choices and concept of loss aversion."
    s "It was because of these 2 studies that I wanted to apply my experience of planning a trip to Japan as well as the decisions that I made during that trip to prospect theory."
    show prospectformula at Position(xpos=0.5, ypos=0.4, xanchor=0.5, yanchor=0.5) with dissolve
    s "Now that was just a surface level description of prospect theory, it has so much nuance and there is so much to uncover-"
    show shawn lookback zorder 10
    pause 0.5
    show shawn shocked zorder 10
    pause 0.5
    show shawn lookback zorder 10
    pause 0.7
    show shawn shocked zorder 10
    pause 0.2
    python:
        for i in range(2):
            renpy.show("shawn lookback", zorder=10)
            renpy.pause(0.05)
            renpy.show("shawn shocked", zorder=10)
            renpy.pause(0.05)
        for i in range(6):
            renpy.show("shawn lookback", zorder=10)
            renpy.pause(0.01)
            renpy.show("shawn shocked", zorder=10)
            renpy.pause(0.01)
    show shawn panicked zorder 10
    s "Okay, maybe it's for the best that we don't go deeper into it haha."
    show shawn encouraging
    s "Let's move onto the next chapter of this game, to my experiences in Japan!"
    stop music fadeout 2.0

# sprites
image shawnjp neutral = "chapter3/sprites/shawn/shawn-jp-default.png"
image shawnjp determined = "chapter3/sprites/shawn/shawn-jp-determined.png"
image shawnjp excited = "chapter3/sprites/shawn/shawn-jp-excited.png"
image mumjp panicked = "chapter3/sprites/mum/mum-jp-panicked.png"
image mumjp worried = "chapter3/sprites/mum/mum-jp-worried.png"

image anthony = "chapter3/anthony-bourdain.png"
image ramen = "chapter3/ramen.jpg"
image gachapon = "chapter3/gachapon.jpg"

# backgrounds
image bg ichiran = "chapter3/ichiran.png"
image bg gachastore = "chapter3/gachapon-store.png"
image bg alley = "chapter3/ramen-alley.png"
image bg haneda = "chapter3/haneda.png"

# images
image hako_arrival = "chapter3/arrival-in-hakodate.png"
image exploring_sapporo = "chapter3/exploring-sapporo.png"
image tsukiji = "chapter3/tsukiji.png"
image curry = "chapter3/soup-curry.png"
image sushicat = "chapter3/sushicat-irl.png"

# endings
image bg taxi = "chapter3/endings/taxi-ending.png"
image bg train = "chapter3/endings/train-ending.png"
image bg store = "chapter3/endings/store-ending.png"
image bg gacha = "chapter3/endings/gacha-ending.png"


label chapter_3:
    $ is_prospect_3 = False
    play music "chapter3/music/scene-1.mp3" fadein 2.0
    scene bg hakodate
    with fade
    s "With the trip mostly planned, we landed in Hakodate without a hitch!"
    s "We mostly enjoyed the fresh seafood and the peace that came with such a rural area of Hokkaido."
    s "The snow was a nice change of pace, and we managed to workaround the language barrier with our best friend of the trip, Google Translate."
    s "Though the next time we had to make a tough decision, it wouldn't be in Hakodate, but in the bustling streets of Sapporo after 4 days in Japan."
    jump sapporo_ramen_alley

label sapporo_ramen_alley:
    scene bg alley
    with fade
    show shawnjp excited at right with moveinright
    s "Ramen Alley... How beautiful!"
    show mumjp worried at left with moveinleft
    m "Boy ah... all the ramen shops here look very run down. Are you sure you want to eat here?"
    m "I saw that there's an Ichiran Ramen nearby. Maybe we could eat there instead?"
    show shawnjp neutral
    s "Mum, the fact that these shoddy shops are still standing should act as a clue to how mouth-watering their ramen should be."
    show anthony at Position(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
    s "I mean the sign here literally says Anthony Bourdain came to the here."
    "(yes, it's a real sign that I saw. It was amazing)"
    m "Aiya, you choose where to eat. But don't come running to me when you get food poisoning arh."
    hide anthony
    show shawnjp determined
    with dissolve
    s "Hmmm, where should I eat?"
    menu:
        "Choose Ramen Alley Restaurant - Uncertain about whether the food is safe or good, but it is possibly really good":
            $ ramen_choice = "alley"
        
        "Choose Ichiran Ramen - Certain of the chain-restaurant food's quality, pretty average ramen":
            $ ramen_choice = "ichiran"


    menu:
        "Are you confident that you have made the optimal choice?"
        "Yes":
            pass
        "No":
            pass

    if ramen_choice == "alley":
        show ramen at Position(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5)
        hide shawnjp
        hide mumjp
        with dissolve
        s "I ignored my mother's pleas and charged headfirst into the restaurant to see what ramen was worthy of Anthony Bourdain's taste buds."
        s "In real life, we did end up eating in that restaurant."
        s "We each got a rich piping hot bowl of miso ramen decked out with thick slices of chashu, bamboo shoots, and bean sprouts for 850 yen."
        s "Way cheaper than any item at Ichiran."
        s "Now I've tried both, and I can stand behind Anthony Bourdain's choice of restaurant because that ramen was one of the best that I have ever had in my lifetime."
        hide ramen with dissolve
    else:
        scene bg ichiran with dissolve
        s "We ended up eating Ichiran because the restaurant looked too shabby for my taste."
        s "The ramen was okay, though I really regretted not eating at the Sapporo landmark that was the ramen alley."
        s "Sometimes I still find myself looking to the stars wondering what the food that Anthony Bourdain came to the here for was like."
        show ramen at Position(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5)
        s "In real life, we did end up eating in that restaurant."
        s "We each got a rich piping hot bowl of miso ramen decked out with thick slices of chashu, bamboo shoots, and bean sprouts for 850 yen."
        s "Way cheaper than any item at Ichiran."
        s "Now I've tried both, and I can stand behind Anthony Bourdain's choice of restaurant because that ramen was one of the best that I have ever had in my lifetime."
    show exploring_sapporo with dissolve
    s "That meal in Sapporo would be one that was hard to forget. We spent the next 3 days sightseeing the many different sights that Sapporo had to offer." 
    show curry at Position(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
    s "We even bought back some of the regional curry to eat at home. On the 5th day, we made it to Tokyo via airplane, landing at around 1230 p.m."
    jump haneda_airport

label haneda_airport:
    stop music fadeout 2.0
    play music "chapter3/music/scene-2.mp3" fadein 2.0 #lower volume
    scene bg haneda
    with fade
    show mumjp panicked at left with dissolve
    m "SHAWN!"
    show shawnjp neutral at right 
    hide mumjp
    with dissolve
    s "Huh!?"
    show mumjp panicked at left with dissolve
    m "TSUKIJI FISH MARKET CLOSES AT 2PM, AND IT'S ALREADY 1230!"
    m "TODAY'S THE ONLY DAY THAT WE CAN GO THERE! WE HAVE OTHER BOOKINGS IN THE MORNINGS FOR THE OTHER DAYS!"
    hide mumjp with dissolve
    show shawnjp determined
    s "Ah dangit, so we have to decide whether to take the train or to take a taxi there, hmm let me think..."
    "Taking a taxi would be more expensive, but it would make us arrive on time." 
    "If we were to take public transport, it would be cheaper and it would take the same amount of time as the taxi, but that's only if the train arrives at the station right as we reach."
    menu:
        "Take a taxi - More expensive, but certain that we will reach on time":
            $ transport_choice = "taxi"
        
        "Take public transport - Cheaper, but uncertain that we will reach on time":
            $ transport_choice = "train"


    menu:
        "Are you confident that you have made the optimal choice?"
        "Yes":
            pass
        "No":
            pass

    if transport_choice == "taxi":
        scene bg taxi with dissolve
        s "We ended up taking the taxi."
        s "We made it to Tsukiji Fish Market at about 1pm, just in the nick of time to experience it in its full glory."
        s "I only realised afterwards that taking the train from the airport to Tsujiki Fish Market would have taken only about 5 minutes more time and would have cost way less money."
        s "It was that day that I learnt how scarily efficient and punctual Japan's train system is."
    else:
        scene bg train with dissolve
        s "We quickly boarded the train and were shocked to see how frequent and quickly trains entered and left the stations."
        s "We managed to reach Tsukiji Fish Market at 1:05 p.m, only about 5 minutes later than if we had taken a taxi."
        s "With our extra money in hand, we walked into Tsukiji Fish Market ready to spend."
    show tsukiji with dissolve
    s "In real life, we did end up succumbing to the certainty effect and taking the taxi to Tsukiji Fish market." 
    s "We minimised the possible loss of missing out on Tsukiji fish market by paying more money for a taxi that would definitely take us there on time."
    s "Although I regret that decision slightly, riding in a Japanese Taxi for the first time was pretty neat. Maybe it's the cognitive dissonance talking."
    
    jump gachapon

label gachapon:
    stop music fadeout 2.0
    play music "chapter3/music/scene-3.mp3" fadein 2.0
    scene bg gachastore
    with fade

    s "After we left Tsukiji Fish Market, I found myself trapped in the snares of a gachapon shop."
    s "My friend had bugged me quite awhile for helping him find a figure from his favourite game, Battle Cats."
    s "His favourite one in particular was something called a sushi cat."
    show gachapon at Position(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
    s "While stumbling around Akihabara, I managed to find a shop that was selling a sushi cat figure for $18."
    s "I found a gachapon machine in the building next to it that dispensed 4 different cat figures, with the exact sushi cat being sold in the shop being a part of this set."
    s "Each figure from the gachapon machine costs $4."
    hide gachapon with dissolve
    show shawnjp determined with dissolve
    s "Dangit... where should I get the sushicat figure from..?"
    menu:
        "Buy from the Gacha machine - A decreased cost of $4, but a 25\% chance of getting sushicat.":
            $ gacha_choice = "machine"
        
        "Buy from the store - A cost of $18, but a confirmed chance of getting sushicat.":
            $ gacha_choice = "store"

    menu:
        "Are you confident that you have made the optimal choice?"
        "Yes":
            pass
        "No":
            pass

    if gacha_choice == "machine":
        scene bg gacha with dissolve
        s "I had decided that $18 was a ridiculous price for something that I could easily get for $4, and hence I decided to gamble."
        s "Although I really did overestimate the lower percentage of 25\%, as it took me about 5 tries to properly get a sushi cat, costing around $20."
        s "I felt a tad bit defeated, holding more plastic cats than I would ever need."
    else:
        scene bg store with dissolve
        s "I did not want to leave my fate in the hands of luck today, and headed into the store to buy the sushi cat."
        s "Though as the $18 dollars left my hand, I couldn't help but feel cheated about how much money I had spent."
        s "But there was also a sense of ease, for I would never know what horros would follow had I been incredibly unlucky at the gachapon"
        
    show sushicat at Position(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
    s "In real life, I succumbed to loss aversion, wanting to minimise any losses, I decided to go to the gacha machine. Thankfully, I was luckier than I should have been that day and got sushicat on the first try."
    hide sushicat with dissolve
    # prospect theory analysis
    $ risk_averse_choices = 0
    if ramen_choice == "ichiran":
        $ risk_averse_choices += 1
    if transport_choice == "taxi":
        $ risk_averse_choices += 1
    if gacha_choice == "machine":
        $ risk_averse_choices += 1

    if risk_averse_choices >= 2:
        # is prospect theory
        $ is_prospect_3 = True
    jump chapter_4

label chapter_4:
    scene bg room with fade
    stop music fadeout 2.0
    play music "chapter1/music/scene8.mp3" fadein 2.0
    if is_prospect_1 and is_prospect_3:
        show shawn confused at right with dissolve
        s "Dang, you really didn't listen to Kahneman and Tversky talk about prospect theory, did you? The majority of choices you made in both planning and in Japan aligned with prospect theory."
        s "You could try again from the start, but if you want to go ahead, then let's pretend that you improved this time around and did not make choices according to prospect theory."

    elif is_prospect_1 and not is_prospect_3:
        show shawn encouraging at right with dissolve
        s "Congratulations! You've had major improvement in decision making after listening to Tversky and Kahneman!"
        s "Now you might be wondering about why this improvement has occurred."

    elif not is_prospect_1 and not is_prospect_3:
        show shawn encouraging at right with dissolve
        s "Stellar decision making as always! I don't think you even needed to learn about prospect theory, but I hope that you at least gained something from that segment."
        s "Now, I'm moving onto why most people would have been less susceptible to prospect theory after learning about it."

    elif not is_prospect_1 and is_prospect_3:
        show shawn confused at right with dissolve
        s "What, how? You somehow made choices that aligned with prospect theory in Japan after making choices that didn't align with it when planning."
        s "I think you might be exploring the different dialogue options, but just in case you aren't, I'm going to move onto why most people would have been less susceptible to prospect theory after learning about it."

    stop music fadeout 2.0
    play music "chapter2/music/scene1.mp3"
    show shawn happy at right with dissolve
    s "With this evaluation of your choices in mind, you might be asking yourself, “If we humans are tied down by our inherent biases and heuristics, how was I able to make better judgments/decisions this time around or make choices that did not align with prospect theory?”"
    show shawn encouraging
    s "Well, this is due to one aspect of human cognition that makes us unique: metacognitive monitoring."
    jump chapter_4_explanation

image metayapping1 = "chapter4/metayapping1.png"
image metayapping2 = "chapter4/metayapping2.png"
image metayapping3 = "chapter4/metayapping3.png"
image metayapping4 = "chapter4/metayapping4.png"
image metayapping5 = "chapter4/metayapping5.png"
image metayapping6 = "chapter4/metayapping6.png"
image metayapping7 = "chapter4/metayapping7.png"
image metayapping8 = "chapter4/metayapping8.png"

image bg end = "chapter4/the-end.png"

label chapter_4_explanation:
    show shawn encouraging 
    s "Before we touch on and define metacognitive monitoring, I'll first run through the history of metacognition."
    show metayapping1 at Transform(size=(960, 540),xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5)  # resize to 800x600
    with dissolve

    s "Metacognition as a concept has been around for quite a long time, being traced as far back to ancient Greece through philosophers like Plato and Socrates, emphasising the importance of self-knowledge and introspection. "
    hide metayapping1 with dissolve
    show shawn happy
    s "In a review of the origins of metacognition by Brown (1987), metacognitive processes have also been recognised and advocated for by education psychologists, like Dewey in 1910 and Thorndike in 1914. "
    s "However, metacognition as a term was coined by John H. Flavell in the early 1970s, based on a term that he coined in a previous paper, ‘metamemory'."
    show shawn encouraging 
    s "He defined metacognition as knowing about, controlling and thinking about cognitive phenomena and processes, or simply put: thinking about thinking (Flavell, 1979)."
    show metayapping2 at Transform(size=(960, 540),xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
    s "His model of metacognitive monitoring has 4 key parts:"
    s "A person's metacognitive knowledge (knowledge and beliefs about cognition),"
    s "a person's metacognitive experiences (feelings about cognition that can happen before, during or after a cognitive task, for example feeling like you won't do well in a test while doing it),"
    s "a person's goals, and finally their actions / strategies to regulate their cognition."
    hide metayapping2 with dissolve
    show shawn happy 
    s "By introducing and talking about prospect theory, the aim of this game I made was to add onto your metacognitive knowledge."
    show shawn encouraging with dissolve
    s "But before I get ahead of myself, moving back to Brown (1987)'s paper inspired more definitions and explorations of metacognition, each with a different emphasis."
    show shawn happy
    s "One such exploration by Shaw (1998) argued that metacognitive knowledge had 3 aspects:"
    show metayapping3 at Transform(size=(960, 540),xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
    s "The first of which is declarative knowledge, which is knowledge about one's own cognitive processes and what factors can influence one's cognition."
    s "The second aspect is procedural knowledge, which is heuristics and strategies for automatic task performance."
    s "Finally, there is conditional knowledge which is knowledge of when and why to apply the previously mentioned aspects of metacognitive knowledge."
    hide metayapping3
    show shawn inspired
    show metayapping4 at Transform(size=(960, 540),xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
    s "He proposed that metacognitive abilities are teachable, with  2 ways being fostering general awareness and improving self-knowledge and regulatory skills."
    show shawn encouraging
    s "In this game, by firstly introducing you to the concept of prospect theory, I did so in hopes of promoting general awareness and self-knowledge of that heuristic we have."
    s "Having that second round of decision making in Japan hence gave you, the player, the opportunity to improve regulatory skills of cognition. "
    hide metayapping4 with dissolve
    show shawn happy
    s "But what does metacognitive monitoring have to do with decision making?"
    show metayapping5 at Transform(size=(960, 540),xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
    s "Well, according to Koriat (2015), metacognitive monitoring has a significant influence on cognitive decision making processes."
    s " This is because it allows people to think about and evaluate the efficiency and efficacy of their current decision making strategies and adjust them accordingly."
    s "In which case, knowing about prospect theory would allow you to reflect on how you evaluate choices and improve the decisions you make based on the outcomes of similar decisions when planning for the trip in the previous round."
    hide metayapping5 with dissolve
    show shawn encouraging
    s "But how exactly can we improve metacognitive monitoring to allow ourselves to improve our decision making processes?"
    show metayapping6 at Transform(size=(960, 540),xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
    s "Well, a study by Huff and Nietfeld (2009) tested 2 methods of improving metacognitive monitoring in students to improve their comprehension skills."
    s "The first being comprehension-monitoring training, where strategies to monitor a student's understanding while reading. "
    s "This, combined with emphasising the importance of monitoring when their understanding fails are taught to the students."
    s "The study found that this method is most effective when demonstrated to students by teachers, followed by opportunities for the students to practice this strategy with feedback."
    hide metayapping6 with dissolve
    s "I tried to adapt this training to a decision-making context with Tversky and Kahneman's feedback on how to remove influences of the effects of prospect theory in decision making. "
    s "The suggestions of reducing emotion, visualising what each option entails and visualising the probabilities were given, and you were given an opportunity to put their strategies into practice during the decision making segment in Japan."
    show metayapping7 at Transform(size=(960, 540),xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
    s "The study also highlights monitoring accuracy training. Did you notice how there have been various moments throughout the game where you have been asked about your confidence in your choices? "
    s "Well, monitoring accuracy training entails comparing a person's confidence in their performance with their actual performance, allowing them to notice inconsistencies."
    hide metayapping7 with dissolve
    show metayapping8 at Transform(size=(960, 540),xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5) with dissolve
    s "Ultimately, the study found that employing comprehension monitoring training by itself or combined with monitoring accuracy training improved metacognitive monitoring."
    show shawn panicked
    s "However, the study also found that employing both strategies leads to overconfidence in the students' performance."
    hide metayapping8 with dissolve
    show shawn happy
    s "And finally, one other way to improve metacognitive monitoring as noted by De Blume (2021) is using deep learning strategies."
    s "Deep learning strategies include ways of problem solving, learning and thinking that require establishing connections between new and already known information,"
    s "critically assessing presented information, "
    s "using inferential skills and rephrasing content all improve metacognitive monitoring."
    show shawn encouraging
    s "The hopefully engaging decision making part of this game, along with its connection to my experiences travelling abroad and examples used hopefully allowed you to establish some of the new information presented here with experiences of your own!"
    s "This would in turn improve your metacognitive monitoring and decision-making skills, reducing the influence of the effects outlined by prospect theory."

stop music fadeout 2.0
play music "chapter4/ending.mp3" fadein 2.0

show shawn neutral
s "But as I conclude this game, I want to firstly highlight that we are defined by our decisions and choices..."
show shawn encouraging
s "whether it be choosing our paths in life, whether or not to buy something, or even deciding what to eat for lunch!"
show shawn happy
s "We are surrounded by decisions, and with the various differing gains, losses and levels of certainty that each choice can bring, we are by extension surrounded by prospect theory and its various effects."
s "And with all of the cognitive processes that happen in our head, learning about it in this diploma and module surrounds me particularly with metacognition by building on my metacognitive knowledge"
show shawn encouraging #with dissolve
s "With that newfound knowledge that I gain each day from class, I find myself monitoring the various ways that I think, learn and make decisions and I hope that through this game, you could have a peek into this experience of metacognitive monitoring too."
show shawn panicked #with dissolve
s "I want to once again state that heuristics such as the ones outlined by prospect theory are not bad, and will not lead to suboptimal outcomes all of the time (at least not as badly as demonstrated in this game)."
show shawn happy #with dissolve 
s "It lightens the limited cognitive resources we have, but there will always be an off chance that it won't lead to the best possible outcome."
show shawn inspired #with dissolve
s "Even though we are only human, and we are bound by our inherent biases and heuristics, what makes us special is our abilities like metacognitive monitoring that lets us rise to the occasion, overcome our inherent flaws to do the best we can and achieve the best possible outcomes through knowledge, training and determination."


hide window with dissolve
scene bg end with dissolve
pause 3.0
scene black with fade
return



