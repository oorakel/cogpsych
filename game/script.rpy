# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Shawn", color="#0080ff") # blue
define m = Character("Mum", color="#800080") # purple
define t = Character("Travel Influencer", color="#008000") # green
define k = Character("Kahneman", color = "#b00000") # red
define tv = Character("Tversky", color = "#ffc800") # yellow

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
    jump chapter_2
    return # important: Ends the chapter

label chapter_2:
    scene bg classroom # Replace with classroom background
    show kahneman # Replace with image
    show tversky at right # Replace with image
    with dissolve

    "The year is 1979. The dominant theory in decision-making is Utility Theory, which posits that people evaluate choices—called prospects—based on their usefulness and likelihood. But cracks in this theory are beginning to show, and two economists are on the brink of proposing something revolutionary."
    "You somehow find yourself in that very classroom where a breakthrough in Economic theory is about to happen. You overhear two prominent economics discussing the prevailing utility theory."

    k "So, Tversky, utility theory defines a prospect as a gamble, a choice with various outcomes and probabilities. It’s elegant, really—expected utility calculates a prospect's attractiveness by averaging each individual outcome’s usefulness with its likelihood. Logical, isn’t it?"
    tv "Logical, sure. But people aren’t calculators, Kahneman. They have emotions, biases, quirks. Why else would someone prefer a guaranteed $100 over a 50\% chance at $250?" # Escaped %
    k "That is most certainly true! You know, I’ve noticed recently that people disproportionately prefer outcomes that are certain when compared to probable outcomes, even when the probable outcome is rationally better using utility theory’s method of calculating expected utility."
    "This was later dubbed the certainty effect."

    if destination == "Sapporo":
        "Do you remember when you chose Sapporo for our travel destination? This choice reflects the certainty effect."
    else:
        "Do you remember when you chose Hakodate for our travel destination? According to the prospect theory’s certainty effect, most people would have chosen Sapporo. This is because Sapporo, despite seeming less fun than Hakodate, comes with the certainty of being able to do what we planned on doing because communication in Sapporo was certain. Despite the fact that Hakodate could have provided a more fun experience, the certainty that Sapporo provided outweighed that outcome and hence made it more attractive according to the certainty effect."

    tv "That is true Kahneman! Another thing I realised is that when I present the same options differently, people flip-flop their preferences. They ignore shared elements and fixate on what’s unique and different between the options, even if both choices have the same outcome framed differently! Haha!"
    "This was later named the isolation effect."
    "Do you remember both times when you had to choose a visa? What if I were to tell you that Starr Insurance and HL Assurance’s insurance plans were objectively identical both times? Starr Insurance reimburses $450 for expenses up to $500 dollars and HL assurance reimburses 90\% of expenses. But framing one as minimising loss and the other as receiving reimbursement could lead to different preferences despite the fact that they were the same both times!" # Escaped %

    k "Have you also noticed that the certainty effect was inverted when it came to scenarios where both options involved losses? People disproportionately prefer choices where decreased losses were possible than choices with confirmed larger losses."
    "This was named the reflection effect."

    if visa == "Company B":
        "Do you remember when you chose company B for the travel visa? This choice reflects the reflection effect."
    else:
        "Do you remember when you chose company A for the travel visa? According to prospect theory’s reflection effect, most people would have chosen company B. This is because there is going to be a definite loss in money in having to buy a travel visa to go overseas. However, company B provided a possible lesser loss compared to company A’s confirmed larger loss. The risk aversion from the certainty effect was flipped on its head to form an aversion to loss."

    "These three observations shaped the 2 economists’ new theory, prospect theory."
    tv "Ah, a fellow decision-maker! You look like someone who has had to make a bunch of tough choices recently. Care to chat about how we make decisions?"

    label prospect_theory_questions: # Loop back here
        menu:
            "What are the processes that take place in decision making according to prospect theory?":
                tv "Well, when we thought about it, Kahneman and I realised that there are 2 phases to decision making, the first of which is the editing phase."
                k "The editing phase simply refers to evaluating your options; grouping outcomes by their similarities, differences, setting a baseline (reference point) to define what is a loss and what is a gain, and finally reframing the options into more objective presentations to reduce biases caused by how choices are presented."
                tv "Indeed. Following this stage, there's the evaluation phase, where individuals assign value to outcomes based on their usefulness and likelihood and decide on what choice to make. Kahneman and I noted that probabilities are often not weighted in a linear fashion, as low probabilities might be overestimated and moderate probabilities might be underestimated. In-line with the certainty effect and the reflection effect, we also noted that losses are weighted more heavily than gains; that is to say a loss hurts way more than an equivalent gain. After all of these values are accounted for, the individual will then make the decision with the highest subjective value."
                jump prospect_theory_questions
            "Were there any issues with prospect theory?":
                tv "Why yes, there were plenty, haha! Our original function did not properly weigh rare events with extremely high impacts, underweighting them despite the fact that people still buy lottery tickets and fear plane crashes!"
                k "Indeed, and our theory overemphasised on the “S-shaped” value function, the function that states that people dislike losses much more than they value equivalent gains. This led to scenarios where the model would point to making the objectively worse option, which does not follow stochastic dominance, a basic rule of decision making that states that if one option is clearly better across all outcomes, it will be preferred."
                if transport == "JR Pass":
                    "Do you remember when you were choosing the transport passes? Stochastic dominance states that most people would buy the tickets individually because it’s way cheaper than buying the JR pass, even though both bring the same outcome."
                tv "We solved this issue by altering our probability weighting function, giving a disproportionate attention to non-likely impactful events, reflecting how people in real life view them."
                k "We also began to calculate probabilities altogether instead of individually, avoiding violating stochastic dominance and allowing our new updated theory, called Cumulative Prospect Theory, published in 1992, to be applied to a larger area of application."
                tv "Previously, prospect theory could only be applied to risky prospects with a small number of outcomes, whereas cumulative prospect theory can be applied to both risky and uncertain prospects where probabilities may not be precisely known!"
                jump prospect_theory_questions
            "Are there any external influences on what guides our decisions with respect to prospect theory?":
                s "Well, yes! There have been multiple studies that used prospect theory as a base to see how certain influences can impact decision making. A study by Campos-Vazquez and Cuilty (2014) found that socio demographic characteristics affect rates of risk loss and aversion, but not the weighing probability function. They also found that a person’s emotional state affects decision making, with sadness increasing risk aversion in gains and risk seeking in losses, amplifying the functions of prospect theory. They also found that anger diminishes the impact of losses, reducing loss aversion significantly. But it was also found that anger does not impact risk aversion in gains in any way. Another study by Abdellaoui et al. (2011) found that even financial professionals behaved exactly according to prospect theory! Though, with a little less loss aversion. One explanation for this decreased loss aversion is desensitisation due to experience and knowledge. Even then, it’s scary to think about how even professionals with years of experience are still subject to this little cognitive bias!"
                jump prospect_theory_questions
            "How can we reduce the influence of the effects of prospect theory in making decisions?":
                k "Well, with the isolation effect in mind, try visualising what each option entails, both similarities and differences."
                tv "And with the influence of emotions on decision making, try to keep calm to minimise risk and loss aversions!"
                k "It would also be helpful to take a moment to think about the actual probabilities of each option, taking a moment to ask yourself if you’re overestimating or underestimating their probability."
                jump prospect_theory_questions
            "That’s all I have to ask, thank you!":
                jump chapter2_conclusion

    label chapter2_conclusion:
        k "Utility Theory had its strengths, but we wanted to build something that reflects real-world behavior. Remember, understanding biases isn’t about avoiding them entirely—it’s about making better decisions despite them."
        show shawn sg at left
        hide kahneman with dissolve
        hide tversky with dissolve
        s "All in all, prospect theory boils down to avoiding risks when it comes to gains, preferring certainty and smaller gains over risk and larger gains, and seeking risks when it comes to losses,  preferring probable smaller losses over certain larger losses."
        s "While prospect theory as a heuristic is certainly helpful in helping us lighten our cognitive load and makes the optimal decisions most of the time, Like Kahneman has said, as with most heuristics, there are times when it won’t give you the best outcome possible (though the outcomes brought about by prospect theory may not be as exaggerated in this game) and understanding prospect"