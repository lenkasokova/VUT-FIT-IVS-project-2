IVS PROJECT 2 - Kalkulačka
---------
Kalkulačka s zakladnými operáciami a funkciami, ktorá sa skladá zo samostatnej matematickej knižnice, grafického uživateľkého rozhrania, prepojenia, inštalátora, uživateľského manuálu a programovej dokumentácie.

Inštalácia
---------
<ol>
<li>Varianta</li>
<ul>
<li>Otvorte súbor <b>calculator 1.0 amd64.deb</b>.</li>
<li>Kliknite na ikonku <b>install</b>.</li>
<li>Zadajte heslo uživateĺa systemu a následne potvrďte tlačidlom <b>authenticate</b>.</li>
<li>Inštalácia prebehne automaticky a kalkulačka sa pridá do zoznamu aplikacií systému.
</ul>
<li>Varianta</li>
<ul>
<li>Otvorte aplikáciu <b>terminal</b>.</li>
<li>Dostante sa do priečinku s výskytom súbor <b>calculator 1.0 amd64.deb</b>.</li>
<li>Zadajte príkaz <code>sudo dpkg -i calculator 1.0 amd64.deb</code> a následne potvrďte tlačidlom enter.</li>
<li>Zadajte heslo uzivateľa systemu a potvrďte tlačidlom <b>enter</b>.</li>
<li>Inštalácia prebehne automaticky a kalkulačka sa pridá do zoznamu aplikacií systému.</li>
</ul>
</ol>

Odinštalácia
---------
Odinštalácia zo systému Linux Ubuntu
<ol>
<li>varianta</li>
<ul>
<li>Otvorte aplikáciu <b>Ubuntu Software</b>.</li>
<li>Prejdite do sekcie <b>Installed</b>a následne do subsekcie <b>Add–ons</b>.</li>
<li>Nájdite kalkulačku s názvom <b>calculator </b>a kliknite na <b>remove</b>.</li>
<li>Zadajte heslo uzivateľa systemu a potvrďte tlačidlom <b>authenticate</b>.</li>
<li>Odinštalácia prebehne automaticky a kalkulačka sa odstráni zo zoznamu aplikacií systému.</li>
</ul>
<li>varianta</li>
<ul>
<li>Otvorte aplikáciu <b>terminal</b>.</li>
<li>Zadajte príkaz <code>sudo apt-get remove calculator</code> a následne potvrďte tlačidlom <b>enter</b>. – Zadajte heslo uzivatela systemu a potvrdte tlacidlom enter.</li>
<li>Odinštalácia prebehne automaticky a kalkulačka sa odstráni zo zoznamu aplikacií systému.</li>
</ul>
</ol>

Profiling
---------
- spúšťa sa príkazom `make profiling < data.txt` z priečinku **src**
- vygenerovany profiling sa bude nachádzať v priečinku **profiling**
- čítať správu z profilingu je možné príkazom `cprofilev -f vystup.prof` ktorý naviguje na URL stránku s vygenerovanou spravou profilingu

**Požiadavky:**
- CProfileV - pokial nie je nainštalovaný v terminali spusťe príkaz `pip3 install cprofilev` 
- Python3 3.8.0 a novšia verzia

Prostredie
---------
Ubuntu 64bit

**Požiadavky:**
- Python3 3.8.0 a novšia verzia
- Python3-tk

Autori
---------
**stayFit**
- xbinov00 Andrej Bínovský
- xlapes02 Zdeněk Lapeš
- xsmeka16 Samuel Smékal
- xsokov01 Lenka Šoková

Licencia
-------
GNU General Public License v3.0
