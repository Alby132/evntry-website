# Regenerates src/pages/hr/pricing.astro from src/pages/pricing.astro.
# Usage: python3 scripts/make-hr-pricing.py src/pages/pricing.astro src/pages/hr/pricing.astro
# If a string on the English pricing page changes, update its Croatian pair below first.
import sys, os
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
T = [
("import BaseLayout from '../layouts/BaseLayout.astro';", "import BaseLayout from '../../layouts/BaseLayout.astro';"),
# FAQ
('q: "Do fans pay any extra fees?", a: "No. The price you set is exactly what fans pay at checkout. Evntry never adds booking fees on the fan side. That\'s one of the reasons fans actually complete the purchase — no sticker shock at the end."',
 'q: "Plaćaju li gosti dodatne naknade?", a: "Ne. Cijena koju postavite je točno ono što gosti plate. Evntry nikad ne dodaje naknade gostima. Upravo zato gosti zaista dovrše kupnju — bez neugodnog iznenađenja na kraju."'),
('q: "Do I own my attendee data?", a: "Yes, completely. Your attendee list — names, emails, purchase history — belongs to you. You can export it anytime. We never share it with third parties or use it for our own marketing."',
 'q: "Jesu li podaci o gostima moji?", a: "Da, u potpunosti. Popis gostiju — imena, e-mailovi, povijest kupnje — pripada vama. Možete ga izvesti bilo kada. Nikad ga ne dijelimo s trećima niti koristimo za vlastiti marketing."'),
('q: "How do I get paid?", a: "Directly through Stripe. For paid tickets, connect your Stripe payout account before publishing. Standard Stripe payment-processing fees are paid by the venue, and payouts follow Stripe\'s normal schedule."',
 'q: "Kako dobivam novac?", a: "Izravno preko Stripea. Za plaćene ulaznice povežite svoj Stripe račun za isplate prije objave. Standardne Stripe naknade za obradu plaćanja plaća prostor, a isplate idu po Stripeovom uobičajenom rasporedu."'),
('q: "Can my free event have paid tickets?", a: "Yes. Your first published event can use free tickets, paid tickets, or both. Evntry charges a 0% platform fee on that event. Standard Stripe processing fees still apply to paid tickets."',
 'q: "Može li besplatni prvi event imati plaćene ulaznice?", a: "Da. Prvi objavljeni event može imati besplatne ulaznice, plaćene ili oboje. Evntry na taj event naplaćuje 0% naknade. Za plaćene ulaznice i dalje vrijede standardne Stripe naknade."'),
('q: "When is my free event used?", a: "Your allowance is used when your first event is published. Drafts do not count. Cancelling or deleting the published event does not grant another free event."',
 'q: "Kada se troši besplatni event?", a: "Besplatni event se troši kada objavite prvi event. Skice se ne računaju. Otkazivanje ili brisanje objavljenog eventa ne daje novi besplatni event."'),
('q: "What happens after my first event?", a: "Contact Evntry about Pro before publishing another event. Pro includes unlimited published events, with pricing agreed individually for your venue and event volume."',
 'q: "Što nakon prvog eventa?", a: "Prije objave sljedećeg eventa javite nam se za Pro. Pro uključuje neograničen broj objavljenih evenata, a cijena se dogovara prema vašem prostoru i broju evenata."'),
('q: "How is Pro priced?", a: "Pro uses custom pricing based on your venue\'s needs and event volume. Book a call and we\'ll agree on a plan that fits your operation."',
 'q: "Kako se određuje cijena za Pro?", a: "Cijena za Pro ovisi o potrebama vašeg prostora i broju evenata. Rezervirajte poziv i dogovorit ćemo paket koji vam odgovara."'),
('q: "Does Stripe charge a separate fee?", a: "Yes. Stripe\'s standard payment-processing fees apply to paid tickets and are paid by the venue. They are separate from Evntry\'s platform fee."',
 'q: "Naplaćuje li Stripe zasebnu naknadu?", a: "Da. Za plaćene ulaznice vrijede standardne Stripe naknade za obradu plaćanja, koje plaća prostor. One su odvojene od Evntry naknade."'),
('q: "Is Evntry available in my country?", a: "Evntry is live in Croatia and expanding across the EU next. Stripe payments work across Europe, so if you run events elsewhere, email hello@evntry.app and we\'ll tell you if we can onboard you now."',
 'q: "Je li Evntry dostupan u mojoj zemlji?", a: "Evntry radi u Hrvatskoj, a sljedeće se širimo po EU. Stripe plaćanja rade u cijeloj Europi, pa ako organizirate evente drugdje, pišite na hello@evntry.app i javit ćemo vam možemo li vas uključiti odmah."'),
# head
('title="Pricing — Evntry"', 'title="Cijene — Evntry"'),
('ogTitle="Pricing — Evntry"', 'ogTitle="Cijene — Evntry"'),
('description="Run your first published event with a 0% Evntry platform fee. Then choose custom Pro pricing tailored to your venue and event volume."',
 'description="Prvi objavljeni event bez Evntry naknade. Zatim Pro paket s cijenom prilagođenom vašem prostoru i broju evenata."\n  lang="hr"\n  alternates={[{ hreflang: \'en\', href: \'https://evntry.app/pricing\' }, { hreflang: \'hr\', href: \'https://evntry.app/hr/pricing\' }, { hreflang: \'x-default\', href: \'https://evntry.app/pricing\' }]}'),
('ogUrl="https://evntry.app/pricing"', 'ogUrl="https://evntry.app/hr/pricing"'),
('canonical="https://evntry.app/pricing"', 'canonical="https://evntry.app/hr/pricing"'),
# body
('<p class="eyebrow">Simple pricing</p>', '<p class="eyebrow">Jednostavne cijene</p>'),
('<h1>First event free.<br>Then <em>simple pricing.</em></h1>', '<h1>Prvi event besplatno.<br>Zatim <em>jednostavno.</em></h1>'),
("Your first published event is on us. When you're ready to run more, we'll tailor Pro to your venue.", 'Prvi objavljeni event je na nama. Kad budete spremni za više, prilagodit ćemo Pro vašem prostoru.'),
('<div class="plan-name">First event</div>', '<div class="plan-name">Prvi event</div>'),
('<div class="plan-tagline">Your first event is on us.</div>', '<div class="plan-tagline">Prvi event je na nama.</div>'),
('<span class="price-free">Free</span>', '<span class="price-free">Besplatno</span>'),
('Run your first published event—free or paid—with <strong>no Evntry platform fee.</strong>', 'Prvi objavljeni event — besplatan ili s plaćenim ulaznicama — <strong>bez Evntry naknade.</strong>'),
('<li>Your first published event</li>', '<li>Vaš prvi objavljeni event</li>'),
('<li>Free or paid ticketing</li>', '<li>Besplatne ili plaćene ulaznice</li>'),
('<li>0% Evntry platform fee</li>', '<li>0% Evntry naknade</li>'),
('<li>QR code door scanning</li>', '<li>QR skeniranje na ulazu</li>'),
('<li>Email ticket delivery</li>', '<li>Ulaznice stižu e-mailom</li>'),
('<li>Live ticket tracking</li>', '<li>Praćenje prodaje uživo</li>'),
('<li>Shareable event and ticket links</li>', '<li>Linkovi za event i ulaznice</li>'),
('<li>Event cover image</li>', '<li>Naslovna slika eventa</li>'),
('class="plan-cta secondary">Start free</a>', 'class="plan-cta secondary">Počnite besplatno</a>'),
('Standard Stripe processing fees apply to paid tickets. A connected Stripe account is required to receive payouts.', 'Za plaćene ulaznice vrijede standardne Stripe naknade. Za isplate je potreban povezan Stripe račun.'),
('<div class="plan-badge">Custom</div>', '<div class="plan-badge">Po dogovoru</div>'),
('<div class="plan-tagline">For venues ready to run more events and grow.</div>', '<div class="plan-tagline">Za prostore koji žele više evenata i rast.</div>'),
('Let’s talk</span>', 'Razgovarajmo</span>'),
('Custom pricing tailored to your venue and event volume.', 'Cijena prilagođena vašem prostoru i broju evenata.'),
('<li>Everything in First event</li>', '<li>Sve iz paketa Prvi event</li>'),
('<li>Unlimited published events</li>', '<li>Neograničen broj objavljenih evenata</li>'),
('<li>Direct support from the founder</li>', '<li>Izravna podrška osnivača</li>'),
('<li>Email blasts to ticket holders</li>', '<li>E-mail obavijesti kupcima ulaznica</li>'),
('<li>Full analytics dashboard</li>', '<li>Potpuna analitika</li>'),
('<li>Promo codes and discounts</li>', '<li>Promo kodovi i popusti</li>'),
('<li>Venue gallery and video</li>', '<li>Galerija i video prostora</li>'),
('<li>Volume pricing, month-to-month</li>', '<li>Cijena po volumenu, iz mjeseca u mjesec</li>'),
('class="plan-cta primary">Book a call</a>', 'class="plan-cta primary">Rezervirajte poziv</a>'),
('>Questions</p>', '>Pitanja</p>'),
('The obvious<br><em>answers.</em>', 'Kratki<br><em>odgovori.</em>'),
('<p class="eyebrow">Get started</p>', '<p class="eyebrow">Krenite</p>'),
('<h2>Start free.<br><em>Scale when ready.</em></h2>', '<h2>Počnite besplatno.<br><em>Rastite kad ste spremni.</em></h2>'),
("Publish your first event with a 0% Evntry platform fee. Book a call when you're ready for more.", 'Objavite prvi event bez Evntry naknade. Rezervirajte poziv kad budete spremni za više.'),
('Create free account →', 'Otvorite besplatan račun →'),
('Book a 30-min call</a>', 'Rezervirajte poziv od 30 min</a>'),
('No credit card required. No commitment.', 'Bez kreditne kartice. Bez obveze.'),
]
for a, b in T:
    if s.count(a) == 0:
        sys.exit(f'MISSING: {a[:80]}')
    s = s.replace(a, b)
os.makedirs(os.path.dirname(dst), exist_ok=True)
open(dst, 'w').write(s)
print('ok', len(T))
