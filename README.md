# Wallet

Wallet records transactions, balances the ledger, manages portfolio, manages the network.
With the help of `Mentor`, Wallet also helps with Insights and Reports.

Classes:

- Wallet
- Ledger
- Transaction
- Account
- Asset

## Journal: Transaction Recording

`Protέgέ`

- Records transactions
- Schedules transactions

## Ledger: Balance Sheet: Balancing the ledger (Credit, Debit)

`Abode`

- Ensures double entry

## Portfolio: Sales & Purchases: Managing assets

### Curator

- Scouts the MARKET to find `Wishlist`ed and `List`ed Assets (Tokens, Currency)
- Manages `Bid`s
- Lists
- Bids
- Wishlists

### Creator

- Creates TOKENS
- Assigns Value to Tokens to create ASSETS

### Author

- Assembles Tokens to create Packages

## People: Network of Vendors, Clients

`Attachέ`

- Maintains `Profile`s of Vendors and Clients

## Market

`Mentor` Regulate Supply and Demand for the market by advising:

- `Curator` to list/bid an asset by calculating MARKET VALUE for all Assets
- `Attachέ` when there is an updated Transaction

## Hierarchy

- Market
    Profiles
        Listings
        Bids
        Wallet
            Balance Sheet (ASSETS = LIABILTIES + EQUITY)
                Accounts - each acc is unique
                    Transactions: TXN-ID (asset,token,package){value} -- from[acc] to[acc] -- | ((asset',token',package'){value'},currency) -- from[acc] to[acc] -- timestamp/scheduletime <({value}-{value'}/currency)=0>
        Portfolio
            Package - {Compounds} charge balancing using chemical bonds
                ionic - electron transfer
                metalic - electron flow
                covalent - electron sharing
                hydrogen - electrostatic attraction - intermolecular
                van der waal - dipolar interactions - intermolecular
            Asset - {Atoms} - stability through nuclear fission and fusion
                complex assets {chemical elements - chemEl} >1(p,n,e)
                protoasset - {protium} - n-e
            token - {subatomic particles} - symmetry preservation through mediated interactions
                composite token (compToken) (p-p)+
                fundamental Token (funToken) - p
            Currency - γ
                Transfer

- Particle
Boson
    higgs {"sp": 0, "ch": 0, "co": 0, "ma": 125100, "ln": 0, "qn": 0, "bn": 0, "pa": h, "pn": 0}
    photon {"sp": 1, "ch": 0, "co": 0, "ma": 0, "ln": 0, "qn": 0, "bn": 0, "pa": γ, "pn": 0}
    gluon {"sp": 1, "ch": 0, "co": r/b/g, "ma": 0, "ln": 0, "qn": 0, "bn": 0, "pa": g, "pn": 0}
    W+ {"sp": 1, "ch": +1, "co": 0, "ma": 80379, "ln": 0, "qn": 0, "bn": 0, "pa": w, "pn": +1}
    W- {"sp": 1, "ch": -1, "co": 0, "ma": 80379, "ln": 0, "qn": 0, "bn": 0, "pa": w, "pn": -1}
    Z⁰ {"sp": 1, "ch": 0, "co": 0, "ma": 91187.6, "ln": 0, "qn": 0, "bn": 0, "pa": z, "pn": 0}
    Graviton {"sp": 2, "ch": 0, "co": 0, "ma": 0, "ln": 0, "qn": 0, "bn": 0, "pa": G, "pn": 0}
Quark
    1st
        up {"sp": 0.5, "ch": +0.667, "co": r/b/g, "ma": 2.2, "ln": 0, "qn": +1, "bn": +0.333, "pa": u, "pn": +1}
        down {"sp": 0.5, "ch": -0.333, "co": r/b/g, "ma": 4.7, "ln": 0, "qn": +1, "bn": +0.333, "pa": d, "pn": +1}
    2nd
        charm {"sp": 0.5, "ch": +0.667, "co": r/b/g, "ma": 1280, "ln": 0, "qn": +1, "bn": +0.333, "pa": c, "pn": +1}
        strange {"sp": 0.5, "ch": -0.333, "co": r/b/g, "ma": 96, "ln": 0, "qn": +1, "bn": +0.333, "pa": s, "pn": +1}
    3rd
        top {"sp": 0.5, "ch": +0.667, "co": r/b/g, "ma": 172900, "ln": 0, "qn": +1, "bn": +0.333, "pa": t, "pn": +1}
        bottom {"sp": 0.5, "ch": -0.333, "co": r/b/g, "ma": 4180, "ln": 0, "qn": +1, "bn": +0.333, "pa": b, "pn": +1}
Lepton
    1st
        electron {"sp": 0.5, "ch": -1, "co": 0, "ma": 0.511, "ln": +1, "qn": 0, "bn": 0, "pa": e, "pn": +1}
    2nd
        muon {"sp": 0.5, "ch": -1, "co": 0, "ma": 105.66, "ln": +1, "qn": 0, "bn": 0, "pa": μ, "pn": +1}
    3rd
        tau {"sp": 0.5, "ch": -1, "co": 0, "ma": 1776.86, "ln": +1, "qn": 0, "bn": 0, "pa": τ, "pn": +1}
Lepton Neutrino
    1st
        electron neutrino {"sp": 0.5, "ch": 0, "co": 0, "ma": 0.0000022, "ln": +1, "qn": 0, "bn": 0, "pa": ve, "pn": +1}
    2nd
        muon neutrino {"sp": 0.5, "ch": 0, "co": 0, "ma": 0.17, "ln": +1, "qn": 0, "bn": 0, "pa": vμ, "pn": +1}
    3rd
        tau neutrino {"sp": 0.5, "ch": 0, "co": 0, "ma": 18.2, "ln": +1, "qn": 0, "bn": 0, "pa": vτ, "pn": +1}
property
    spin - sp
    charge - ch
    color - co
    mass - ma
    lepton number - ln
    quark number - qn
    baryon number - bn
    particle flavor - pa
    particle number - pn
