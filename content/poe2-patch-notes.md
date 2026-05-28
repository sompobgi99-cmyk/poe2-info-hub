# Path of Exile 2 — Patch Notes เรียงตามวันที่

> ทุกอัปเดตเรียงตามวันที่ (ใหม่สุด → เก่าสุด) | Source: GGG, poepatchnotes.com

---

## 28 พฤษภาคม 2026 — 0.5.0 Patch Notes อัปเดต (Last-Minute Changes)

> GGG อัปเดต patch notes เพิ่มเติมก่อนเปิดเซิร์ฟเวอร์ 29 พ.ค.

### 🔧 ระบบ Totem & Mana Cost

- **Ancestral Bond Keystone:** Totem Limit x2, ไม่ต้องใช้ Charges วาง Totem, Totems จอง 75 Spirit ต่อตัว — ที่สำคัญ: ถึง Spell Totem จะมี Spell tag แต่การอัญเชิญ Totem เองไม่ใช่ Spell — ดังนั้น mod ที่เพิ่ม cost ให้ spells จะไม่เพิ่ม cost การวาง Spell Totem
- **Skills ที่ไม่เคยมี cost** ตอนนี้ cost 0 Mana — ทำให้ +cost modifiers ทำงานกับมันได้ — รวมถึง default weapon attacks, item-inherent skills, และ triggered skills จาก Support Gems

### 🩸 Blood Mage — Sanguine Tides ปรับ

- รับ 1 Life Flask Charge ต่อ 2% Life ที่ใช้ (เดิม 4%)
- เมื่อ hit enemy ขณะ Life Flask เต็ม → กิน 40% charges → ได้ 1% damage เป็น Physical ต่อ charge **นาน 5 วิ** (เดิม 3 วิ)
- **Flasks ไม่ recover Life เลย** (เดิม 50% less — ตอนนี้ 100% less!)

### 📦 Strongbox ปรับปรุง

- Additional Chest level modifier: +1 (จาก +1-2)
- Prefix "Casts Chaos Barrages" และสายสกิล → เพิ่ม 10-20% more Rarity of Contained Items
- Prefix ใหม่ 2 แบบ: (1) Strongbox Monsters มี 40-60% increased Rarity + 40-60% more Rarity of Contained Items, (2) 15-30% increased Monster Effectiveness + 20-30% more Quantity

### 🕯️ Ritual ปรับ

- หลังจากฆ่า King in the Mists ใน Act 1 Freythorn → จะไม่ได้รับ Ritual Altar rewards อีก

### ❄️ Eye of Winter

- แสดงจำนวน shard projectiles ที่ยิงต่อวินาทีระหว่างบิน
- จำนวนนี้ปรับด้วย additional projectiles ได้แล้ว

### 🐛 Bug Fix — Minion Damage

- แก้ bug ที่ minion damage bonus vs non-unique enemies (ตั้งแต่ 0.3) ทำงานผิดพลาด
- ผลลัพธ์: early game minion damage แทบไม่เปลี่ยน, **late-game +25-35%** vs non-unique, **late-game +20-25%** vs unique
- โบนัสนี้จะไม่แสดงในตัวเลข damage ของ minion skills

---

## 26 พฤษภาคม 2026 — 0.5.0 Patch Notes อัปเดต

> GGG เพิ่ม/แก้ไข patch notes — 3 วันก่อนเปิดเซิร์ฟเวอร์

### 🛠️ ระบบคราฟ & คุณภาพชีวิต

- **Kalguuran Supports 7 อัน:** Concussive Runes, Fist of Kalguur, Healing Runes, Runeforged Blades, Runic Extraction, Runic Infusion, Scouring Flame
- **Trade Market Quick Search:** Shift+Alt+Click ไอเท็ม → เติม filter ค้นหาตลาดอัตโนมัติ — สำหรับ Rare items ปิด/เปิด mod ทีละตัวเพื่อดูผลต่อราคาได้ (controller: กด Y/Triangle)
- **Jeweller's Orbs (Lesser/Greater/Perfect)** ใช้กับ items ที่มี skills ในตัวเพื่อเพิ่มซ็อกเก็ตได้แล้ว — ถ้ามีหลายสกิลจะเพิ่มให้ทุกสกิล
- **Command `/reclaimexpeditioninventories`** — เรียกของคืนจาก inventory เก่า (Recombinator, Expedition Vendors)

### 🗺️ Atlas & Endgame ปรับปรุง

- Click Town บน Atlas → วาร์ปทาง waypoint, Ctrl+Click quick travel
- **Unforeseen Consequences Unique Tablet:** ไม่มี 4-6 additional Rare Monsters จาก Abysses อีกแล้ว (Divine Orb ทำให้แย่ลงได้)
- Act 4 bosses หลายตัวปรากฏใน Stone Circle Map mechanic ได้แล้ว
- **Allies in Presence mods** (เช่น Sceptres, Grip of Kulemak) ไม่ stack ในปาร์ตี้อีก — ยกเว้น Leer Cast Unique Helmet

### 🌳 Passive Tree — เพิ่ม Clusters ใหม่

- Armour applies to Elemental Damage + faster start of ES Recharge
- Hybrid: Armour/Elemental + Deflection
- Hybrid: Deflection + Faster Start ES Recharge
- Armour + Evasion clusters ใหม่

### ⚖️ Passive Tree — Notable ปรับปรุง

- **Backup Plan:** +20% Armour/Evasion, Evasion if hit recently 40% (เดิม 50%), Armour if not hit 40% (เดิม 50%)
- **Defiance:** +20% Armour/Evasion (เพิ่ม), Low Life +80% (เดิม 120%)
- **Insulated Treads / Strong Chin:** +25% Armour/Evasion เพิ่มเติม
- **Iron Slippers:** 2 Armour/1 ES on Boots (เดิม 3)
- **Subterfuge Mask:** 1 Evasion/1 ES on Helmet (เดิม 2)
- **Tolerant Equipment:** +15% Armour/Evasion
- **Wild Cat:** 12% Evasion as Deflection (เดิม 10%)
- Small Deflection passives: 8% (เดิม 6%)

### ⚔️ Skills & Items

- **Barkskin:** 50% ES Lost as Armour ที่ lv8 (เดิม 32%), สเกลถึง 62% ที่ lv20 (เดิม 44%)
- **Mark of Siphoning:** Leech Mana 8% of Physical Attack Damage
- **Mark of Siphoning II:** Leech Mana 8% + Leech Life 8% of Physical Attack Damage
- **Gravebind Unique Gloves:** 15-20% Increased Rarity of Items Found, Your other Rarity mods do not apply — มีผลกับของที่มีอยู่แล้ว
- **Tribal Medicine quest:** ปรับปรุงรางวัล — "Happy shark hunting"

### 🎨 MTX & Art

- Originator's Weapon Effect รองรับ PoE 2
- Celestial Emperor Rare Finisher Effect รองรับ PoE 2
- 3D art สำหรับ Rise of the Phoenix

### 🐛 Bug Fixes

- **Fire Skills + Spell Totems:** ไม่ generate Raging Spirits อีก
- **Fire Skills + Align Fate Visages:** ไม่ generate Raging Spirits
- **"Lord's" Spirit mod:** แก้ค่าทับซ้อน — 20-26% (เดิม 30-36%)
- **Chaos Inoculation:** แก้ bug stun/ailment threshold — ผู้เล่น CI ไม่ immune Heavy Stuns แบบผิด ๆ แล้ว
- **Eternal Youth + 0 ES:** แก้ Life Recharge ไม่สนใจ ES Recharge delay
- **Gore Spike:** Critical Damage Bonus แสดงใน skill stats panel แล้ว
- **Queued skills:** แก้อัปเดต target ไม่ได้
- **Killing Palm/Staggering Palm:** แก้ dash พลาด target
- **Arbiter of Ash:** แก้ projectiles หายเมื่ออยู่ไกลเกินไป

---

## 25 พฤษภาคม 2026 — 0.4.0l

**🔚 ปิดลีก Fate of the Vaal**
- สิ้นสุด Fate of the Vaal League — ตัวละครและความคืบหน้าจะถูกย้ายในอีกไม่กี่ชั่วโมง
- เพิ่ม [Passive Skill Tree บนเว็บไซต์](https://pathofexile2.com/game/passive-skill-tree) ให้ดูออนไลน์ได้
- เตรียมพร้อมสำหรับ Runes of Aldur league — เศรษฐกิจใหม่เริ่มต้น

---

## 21 พฤษภาคม 2026 — 0.5.0 Content Update: Return of the Ancients

> Patch Notes ฉบับเต็ม — อ่าน 97 นาที | [Official Thread](https://www.pathofexile.com/forum/view-thread/3932540)

### 🪨 Runes of Aldur League
- **Remnants** ระบบเลือกสูตรรูน → เลือกรางวัล → สู้ศัตรูเสริมพลัง → รับของ
- NPC Farrow + 4 เควสต์ใหม่ในแคมเปญ
- Verisium metal สกุลเงินใหม่
- **Verisium Runeforging** — Runeforge เกราะ + อาวุธ Unique (<lv55) ให้อัปเกรด base type
- **Runic Ward** — ค่าป้องกันใหม่ (ทำงานเมื่อ HP เหลือ 1, รีเจนแยก)
- **Alloys 13 ชนิด** — คราฟ modifier ใหม่บนไอเท็ม
- **Ancient Runes 13** (โบนัสอาวุธ), **Mythical Runes 13** (เลเวล 15+), **Fluxes 3** (เปลี่ยน resistance), **Meta runes 15**, **Unique-destruction runes 60+**, **Runic Ward runes 15+**
- **Kalguuran Skills 23 สกิลใหม่** — ใช้ Runic Ward แทนมานา
- **Kalguuran Supports 7 อัน**
- Expedition Remnants → กลายเป็น Remnants ของ Runes of Aldur
- Endgame ใหม่: ออกทะเลสำรวจเกาะ + สุสาน Kalguuran + อุกกาบาต Verisium
- Hub: Ruins of Kingsmarch (ตะวันออกเฉียงใต้)
- 4 Faction Leaders: Medved, Vorana, Uhtred, Olroth
- Pinnacle Boss ใหม่ (ล็อกจาก Olroth)
- **Challenges แรกของ PoE 2** — 8 ภารกิจ → ชุดเกราะ Knight of Aldur + Totem Pole

### 🗺️ Origins of Divinity — Endgame ยกเครื่อง
- **Fortress** — โผล่จากพื้นดินเมื่อทำ Tower แรกเสร็จ
- Maps ใน Fortress → Atlas Passive Points (แทนที่วิธีเดิม)
- **Atlas Passive Tree 300+ nodes** — ปลดล็อกทั้งต้นได้
- Multi-choice nodes — เปลี่ยนได้ตลอดเวลา ไม่ต้อง respec
- Ancient Modifiers 40+ — ปรากฏบน maps
- Gateway Maps 3 + บอสใหม่ 2
- Citadel Maps 2 + บอสใหม่ 2 → keys to new Pinnacle
- **Arbiter of Divinity** — Pinnacle Boss ใหม่!
- แผนที่ Endgame ใหม่ 30 พื้นที่
- Arbiter of Ash + Burning Monolith → ย้ายเข้า Fortress
- Crisis fragments มีเวอร์ชั่น Quest ใน Enigma chambers inside Fortress
- Atlas ถูก reset — ต้องทำ Origins of Divinity storyline เพื่อรับ Atlas points

### 🌀 Delirium รีเวิร์ค
- Hub: The Withered Willow (ตะวันตกเฉียงใต้)
- Progress Bar — ความลึกในหมอก + เวลาที่เหลือ
- เดินตามทิศทางหมอก → ไปหา Map Boss (100% delirious)
- กระจกสีแตกเมื่อถึงความลึก → activate encounters ใหม่
- **Loathsome Mire** — sub-area ใหม่, Amulet base types ใหม่
- Liquid Emotions คราฟ Jewels ได้
- **Grand Mirrors** — duplicate map boss → ฆ่าทั้งคู่ → Trial of Madness
- **Trial of Madness** — เลือก map → fog แพร่ (10-200% delirious)
- Simulacrum: 7 waves → key to Delirium Pinnacle ใหม่
- Ancient Emotions 10 (Timelost Jewels) + Potent Emotions 3
- Delirium Uniques บางชิ้น → Raven-Touched (instill ได้)

### 💎 Breach รีเวิร์ค
- Hub: Monastery of the Keepers (ใต้)
- Progress Bar — เวลาก่อน Breach ปิด
- **Stabilised Breach** — เมื่อถึง 100%
- Vruun, Marshal of Xesht — บอสใหม่
- **Genesis Tree** — Wombgifts + Hiveblood → Rings/Amulets/Belts
- Ring ใหม่ 6, Amulet ใหม่ 4, Belt ใหม่ 4 (จาก Genesis Tree เท่านั้น)
- Catalysts จาก Genesis Tree เท่านั้น + 12 Catalysts ใหม่สำหรับ Jewels
- Breachstone splinters → special wombgift → Breachstone ที่ Genesis Tree
- **Breach Domains** — Breach Hives, Sky Hives, Sky Fortresses
- Tul + Esh → key to Breach Pinnacle

### 🕯️ Ritual รีเวิร์ค
- Hub: Caer Tarth (ตะวันตก)
- ตั๊กแตนชี้ทางไป Altar ถัดไป
- Endgame Ritual rewards → Unique หรือ Omens เท่านั้น
- Tribute เหลือ → สังเวยเป็น Audience with the King
- **Head of the King** key → Rite of the Nameless
- **Rite of the Nameless** — 5 maps ต่อเนื่อง, monsters จากทุก map ปรากฏซ้ำ
- **Queen in the Mists** — บอสใหม่ (ต้อง unlock Atlas node)
- Freythorn Rituals ไม่มี deferred items

### 👁️ Abyss ปรับปรุง
- รอยแยก Abyss ใหญ่บน Atlas → ปิดแล้วได้ Abyssal Depths เสมอ
- Kulemak's Invitation ให้ Map owner เสมอ
- Abyss Omens ไม่ดรอปต่ำกว่า lv65
- ปรับดาเมจ Meteoric Demise + Lithomantic Runes delay

### 🔱 Fate of the Vaal → Core
- พบ Ancient Beacons 6 ใน Act 3 + อีก 6 ใน Interludes
- Hub: Lira Vaal (ตะวันออกเฉียงเหนือ)
- Atlas Passive Tree สำหรับ Vaal โดยเฉพาะ
- ป้องกัน "snake" strategy — ห้องที่ต้องลบกลายเป็น Path rooms
- Rooms อัปเกรดเป็น Tier 4 ได้
- Infusers 4 ชนิด: Armourer's, Blacksmith's, Arcanist's, Catalysing
- ใช้ได้เฉพาะ items ≥20% Quality
- ปรับ Vaal Cultivation Orb outcomes บน Unique หลายชิ้น
- Energised Crystals เพิ่มเป็น 60, Medallions เพิ่มเป็น 6

### ⚔️ Expedition ปรับใหญ่
- Expedition ถูกปิดชั่วคราวใน Standard (รวมกับ Runes of Aldur)
- Recombinator ถูกปิด — Omen of Recombination ถูกลบ
- Forgotten By Time tablet หยุดดรอป
- Explosives รอจนมอนสเตอร์จากระเบิดก่อนหน้าตายเกือบหมด
- ใช้ Currency จาก stash ซื้อของ Expedition Vendor ได้
- Legacy Expedition Currency → ขายเป็น Gold
- `/reclaimexpeditioninventories` เรียกของคืนจาก inventory เก่า

### 🎯 Masters of the Atlas
- ระบบ Ascendancy สำหรับ Atlas — 3 Masters:
  - **Doryani's Science** — ปลดล็อกจาก clearing corruption nexus
  - **Hilda's Hunting** — ปลดล็อกจาก Hilda's Campsite
  - **Jado's Spycraft** — ปลดล็อกจาก anomaly map
- Master แต่ละคน 12 nodes → เลือก 4 พร้อมกัน
- เปลี่ยนเมื่อไหร่ก็ได้, ทั้ง 3 Masters ทำงานพร้อมกัน

### 🗺️ Atlas & Map Changes
- ค้นหา Atlas Map ได้
- Zoom out ได้ไกลขึ้น
- Click Town → waypoint, Ctrl+Click quick travel
- 2 versions ของ Pinnacle Boss: Quest vs Infinite Farm
- Tablets ชนิดเดียวกันใช้ซ้อนกันเพิ่ม content ได้
- Empty tablet slots → random league content
- **Waystones ต้อง identify** ก่อนใช้
- Orbs of Chance ใช้กับ Tablets ได้
- Monster Rarity stat ใหม่
- ปรับ Waystone Modifier bonuses, Prefix/Suffix ใหม่
- Shrine duration: 45 วินาที (base)
- Strongbox "Contains Identified Items" ถูกลบ
- Tablet modifiers ที่ไม่ทำงานแล้ว → disabled
- Atlas completion แชร์กับ party members

### 👊 New Ascendancies
- **Martial Artist** (Monk) — ภาพลวงตา, ระฆัง, รูนบนร่างกาย
- **Spirit Walker** (Huntress) — วิญญาณสัตว์, ปราบบอสมาเป็นเพื่อน

### 🛠️ Quality of Life
- **Build Guides ในเกม** (ไฟล์ .build)
- **Trade:** Shift+Alt+Click ดูราคา + toggle mods
- Fragment Stash Tab รองรับแล้ว
- ข้ามบทสนทนา NPC ด้วย Escape
- Reforging Bench ที่ Trial of Sekhemas
- ปาร์ตี้: ชุบเพื่อนหลังฆ่าบอส

### 🆕 Items & Gems (0.5.0)
- Lineage Supports ใหม่ 23 ตัว (Arbiter's Reach, Breachlord's Amalgam, Trickster's Shard, Vorana's Siege ฯลฯ)
- Unique Items ใหม่ 42 ชิ้น (Mageblood, Berek's Grip/Pass/Respite, Facebreaker, Brutus' Lead Sprinkler, Loreweave, Voices, Split Personality, The Raven's Flock, Gatecrasher, Opportunity, Redemption ฯลฯ)
- Idols ใหม่ 8 (จาก Azmeri Spirits)
- Minion Splash Support I & II

### ⚡ Ascendancy ปรับปรุง (0.5.0)
**Acolyte of Chayula:** Leech เพิ่ม Life 15→20%, Mana 15→20%
**Blood Mage:** Vitality Siphon 10→20% Leech, Sanguine Tides flask 4%→2% Life per charge
**Chronomancer:** Rapid River ถูกลบ, Now and Again ใหม่ (Echo/Repeat 20%), Phased Form ใหม่ (ลดดาเมจ 30% + ดีเลย์ 4 วิ), Inevitable Agony รีเวิร์คเป็น Life Loss
**Gemling Legionnaire:** Crystalline Potential ถูกลบ, Essence of Virtue ใหม่, Advanced Thaumaturgy — gems ทุกเม็ดมี additional quality effect
**Pathfinder:** Overwhelming Toxicity 35→50% less Poison Duration
**Witchhunter:** Obsessive Rituals 35→50% less Armour/Evasion

### 🌳 Passive Tree ปรับปรุง (0.5.0)
- Companion-themed 19 nodes, Life Recoup 9 nodes
- Ancestral Bond: Totem Limit x2, no charges, 75 Spirit each
- Vaal Pact: 50% more Life Leech, 67% less Leech speed
- Energy Shield Recharge Rate → faster start of ES Recharge ทั่วทั้ง tree
- Notable 30+ ตัวถูกปรับ

### 🗡️ Skill Changes (0.5.0)
- Cull the Weak รีเวิร์ค (109-281% damage, dash +15%)
- Comet ดาเมจลด, Barkskin ES→Armour buff
- Banners ไม่มี movement penalty

### 👹 Monster & Quest (0.5.0)
- Culling Threshold 30→35%, Leech resistance ลดลง
- Act 3 จัดเรียงพื้นที่ใหม่, Act 2 ตัด Dreadnaught Vanguard
- Waterways เดินเหยียบแทนดึงคันโยก
- Monster density ครึ่งหลังลดลง

### 🎮 UI & QoL (0.5.0)
- Accessibility: popup size, dedicated dodge roll keybind
- Click-to-move ไม่ interrupt channeling
- MTX: 20+ ชุดเกราะ, 50+ Wings/Cloaks รองรับแล้ว

### 🐛 Bug Fixes (0.5.0) — 100+ รายการ
- Minion damage +25-35% late-game, Chaos Inoculation stun fix
- Hollow Palm Technique แก้, Bleed ใช้กับ Spell Hits ได้
- Boss/Delirium/Abyss/UI fixes จำนวนมาก

---

## 14 มีนาคม 2026 — 0.4.0k (Hotfix)

- แก้ไขปัญหาต่าง ๆ จาก Fate of the Vaal League

---

## 7-10 มีนาคม 2026 — 0.4.0j → 0.4.0i → 0.4.0h (Hotfixes)

- แก้ไข Temple mechanics, balance adjustments, bug fixes

---

## 28 กุมภาพันธ์ 2026 — 0.4.0g (Hotfix)

- ปรับสมดุล Vaal Temple และ Atziri encounter

---

## 20-25 กุมภาพันธ์ 2026 — 0.4.0f → 0.4.0e → 0.4.0d (Hotfixes)

- แก้ไข Temple console issues, room spawning fixes
- ปรับ Architect fights และ Locus of Corruption

---

## 18 กุมภาพันธ์ 2026 — 0.4.0c

- ปรับปรุง Temple navigation และ room connections
- แก้ไข Vaal Orb duplication exploit

---

## 15 กุมภาพันธ์ 2026 — 0.4.0b

- Temple progress persistence fixes
- ปรับดาเมจ Architect bosses

---

## 12 ธันวาคม 2025 — 0.4.0: Last of the Druids

### 🐺 Druid — คลาสใหม่
- Shapeshifting: Werewolf, Bear, Wyvern
- Elemental + physical hybrid

### 🏛️ Fate of the Vaal League
- สร้าง Vaal Temple → อัปเกรดห้อง → Locus of Corruption (double Vaal)
- Atziri, The Red Queen — Pinnacle Boss
- Architect's Orb + Vaal Infuser

### ✨ New Ascendancies
- Oracle (Druid)
- Shaman (Druid)
- Sorceress Ascendancy ใหม่

### 🛠️ Changes
- Druid ใช้เวลาพัฒนานานเพราะความซับซ้อนของ shapeshifting
- Endgame rework เลื่อนไป 0.5

---

## 19-28 พฤศจิกายน 2025 — 0.3.2c → 0.3.2b → 0.3.2a (Hotfixes)

- Abyss balance adjustments
- Kulemak encounter fixes

---

## 12 พฤศจิกายน 2025 — 0.3.2

- Abyssal Depths generation improvements
- Desecrated Modifiers balance pass

---

## 5 พฤศจิกายน 2025 — 0.3.1

- Abyss league mechanic fixes
- Act 4 boss tuning

---

## 28 สิงหาคม 2025 — 0.3.0: Rise of the Abyssal

### 👁️ Abyss League
- รอยแยก Abyss ใน Maps → Abyssal Bones → Well of Souls
- Abyssal Depths (sub-area + boss)
- Vessel of Kulemak — Pinnacle
- Unique: Grip of Kulemak, Darkness Enthroned

### 📜 Act 4
- Act 4 สมบูรณ์ — Kingsmarch
- Act 5 ชั่วคราว (reuse Act 1-3)
- ยกเลิก Cruel Difficulty

---

## 19-26 กรกฎาคม 2025 — 0.2.3c → 0.2.3b → 0.2.3a (Hotfixes)

- Huntress balance pass, Breach stability fixes

---

## 10 กรกฎาคม 2025 — 0.2.3

- Breachstone drop rate adjustments
- Xesht encounter tuning

---

## 28 มิถุนายน 2025 — 0.2.2

- Breach mechanic rewards rebalance

---

## 15 มิถุนายน 2025 — 0.2.1

- Huntress skill balance
- Campaign progression fixes

---

## 24 เมษายน 2025 — 0.2.0: Huntress

### 🏹 Huntress — คลาสใหม่
- Spear-based, DEX class
- Combo-oriented playstyle

### 🌀 Breach Rework
- มือแดง, วงขยาย, Hiveborn
- Breachstones → Breachlord domains
- Xesht, We That Are One — Pinnacle

---

## มีนาคม-เมษายน 2025 — 0.1.2 → 0.1.3 → 0.1.4 (Hotfixes)

- Multiple hotfixes: balance, crashes, server stability
- Trade market improvements

---

## 25 มกราคม 2025 — 0.1.1

- Post-launch balance + bug fixes
- Performance optimizations
- Server stability

---

## 6 ธันวาคม 2024 — 0.1.0: Early Access Launch

### 🎮 เปิดตัว
- 6 คลาส: Warrior, Ranger, Monk, Mercenary, Witch, Sorceress
- 3 Acts (เล่นซ้ำ Cruel)
- Passive Tree 1,500+ nodes
- WASD Movement + Dodge Roll
- ระบบ Skill Gem ใหม่
- Cross-play + Cross-progression

### 🗺️ Endgame
- Atlas of Worlds — Maps + Waystones
- League Mechanics: Breach, Delirium, Ritual, Expedition
- Arbiter of Ash — Pinnacle Boss

---

*เอกสารนี้ถูกสร้างเมื่อ 28 พฤษภาคม 2026 — จาก poepatchnotes.com + GGG Official Forums*
