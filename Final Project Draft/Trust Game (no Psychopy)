import sys
import random

print('Here are the instructions to the game you will play with a partner. In this game you are the “investor.”')
print('You start each round with $1 and must decide whether to keep or invest it. By keeping the $1, your partner receives $0.') 
print('If you invest, you transfer the $1 to your partner. By doing so, the $1 is tripled to $3.')
print('Your partner can split the $3 and you both receive $1.5.')
print('Or, your partner can keep the $3 for themselves and you recieve nothing.')
print('If you understand the rules and consent to the game, enter "y". If you do not wish to play enter "n"')
x = input('Enter "y" or "n": ')
if x == 'y':
    #participant:
    participant_total_earnings = 0.00
    participant_money_trial = '$1.00'

    #bot/partner:
    partner_trial_investment = 0.00
    partner_total_earnings = 0.00
    
    i = 1
    while i < 21:
        print('Round ' + str(i) + ': $1.00')
        q = input('Enter "k" for "KEEP" or "i" for "INVEST": ')
        if q == 'k': 
            print('You KEPT the $')
            participant_total_earnings = participant_total_earnings + 1.00 
            print("Your round earnings: $1.00 Partner A's round earning: $0.00")
            print('Sum total earnings = $' + str(participant_total_earnings) + '0')
        elif q == 'i':
            partner_trial_investment = partner_trial_investment + 3.00
            neutral_partner_decsion = ['keep', 'share']
            a = random.choices(neutral_partner_decsion, weights=(1,3), k=1)
            if a == ['keep']:
                partner_total_earnings = partner_total_earnings + 3.00
                print('Partner A KEPT the $')
                print("Your round earnings: $0.00 Partner A's round earning: $3.00")
                print('Sum total earnings = $' + str(participant_total_earnings) + '0')
            elif a == ['share']:
                partner_total_earnings = partner_total_earnings + (3.00/2.00)
                participant_total_earnings = participant_total_earnings + (3.00/2.00)
                print('Partner A SHARED the $')
                print("Your round earnings: $1.50 Partner A's round earning: $1.50")
                print('Sum total earnings = $' + str(participant_total_earnings) + '0')
        else: 
            i = i - 1
        i += 1
        if (i == 21):
            break 
    print('That was the final round with partner A')
    print('Your sum total earnings after 20 rounds playing with partner A= $' + str(participant_total_earnings) + '0')
elif x == 'n':
    print('Here is your alternative assignment') 
else: 
    print('Wrong Letter')
