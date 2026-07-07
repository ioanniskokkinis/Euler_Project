def exchange_money(budget, exchange_rate):
    """Υπολογίζει πόσα ξένα νομίσματα παίρνεις."""
    # Αν έχεις 100€ και η ισοτιμία είναι 1.2, παίρνεις 100 * 1.2
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Υπολογίζει τι σου μένει στο αρχικό σου νόμισμα."""
    # Απλή αφαίρεση: όσα είχες μείον όσα έδωσες
    return budget - exchanging_value

def get_value_of_bills(denomination,number_of_bills):
    """"""
    #
    return denomination * number_of_bills
    if((denomination % number_of_bills) >= 0):
        print("Keep the change")
        


def get_number_of_bills(amount, denomination):
    """Υπολογίζει πόσα χαρτονομίσματα θα πάρεις (ακέραιο)."""
    # Χρησιμοποιούμε floor division (//) για να πάρουμε μόνο ολόκληρα χαρτονομίσματα
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """Υπολογίζει το 'ρέστα' που δεν συμπληρώνουν χαρτονόμισμα."""
    # Εδώ χρησιμοποιούμε το modulo (%)
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Το πιο σύνθετο: Υπολογίζει τη μέγιστη ανταλλάξιμη αξία 
    λαμβάνοντας υπόψη την προμήθεια (spread) και τα διαθέσιμα χαρτονομίσματα.
    """
    # 1. Υπολογίζουμε την πραγματική ισοτιμία με το spread (π.χ. +10%)
    actual_rate = exchange_rate * (1 + spread / 100)
    
    # 2. Πόσα ξένα νομίσματα μπορούμε να αγοράσουμε συνολικά;
    total_foreign_currency = budget / actual_rate
    
    # 3. Πόσα ολόκληρα χαρτονομίσματα (της συγκεκριμένης αξίας) βγαίνουν;
    bill_count = int(total_foreign_currency // denomination)
    
    # 4. Επιστρέφουμε τη συνολική αξία ΜΟΝΟ των ολόκληρων χαρτονομισμάτων
    return bill_count * denomination