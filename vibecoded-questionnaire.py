import random


FRAGOR = {
	"lätt": [
		("Vad heter Sveriges huvudstad?", ["Göteborg", "Stockholm", "Malmö"], "B"),
		("Hur många ben har en spindel?", ["6", "8", "10"], "B"),
		("Vilken färg får man om man blandar blått och gult?", ["Grön", "Lila", "Orange"], "A"),
	],
	"medel": [
		("Vilken planet kallas den röda planeten?", ["Venus", "Mars", "Jupiter"], "B"),
		("Vad heter Sveriges längsta älv?", ["Klarälven", "Dalälven", "Göta älv"], "A"),
		("Vilket grundämne har den kemiska beteckningen Fe?", ["Fluor", "Järn", "Fosfor"], "B"),
	],
	"svår": [
		("Vilket år lämnade Sverige Kalmarunionen?", ["1397", "1523", "1611"], "B"),
		("Vad är det kemiska tecknet för volfram?", ["V", "W", "Vo"], "B"),
		("Vilken är den minsta primtalsfaktorn i 221?", ["11", "13", "17"], "A"),
	],
}


def spela():
	print("\n=== Välkommen till frågesporten! ===")
	print("Välj svårighetsgrad: lätt, medel eller svår")

	while True:
		niva = input("> ").strip().lower()
		if niva in FRAGOR:
			break
		print("Ogiltigt val. Skriv lätt, medel eller svår.")

	fragor = FRAGOR[niva][:]
	random.shuffle(fragor)
	poang = 0

	for nummer, (fraga, alternativ, ratt_svar) in enumerate(fragor, start=1):
		print(f"\nFråga {nummer}/{len(fragor)}: {fraga}")
		for bokstav, text in zip("ABC", alternativ):
			print(f"  {bokstav}) {text}")

		while True:
			val = input("Ditt svar (A, B eller C): ").strip().upper()
			if val in ("A", "B", "C"):
				break
			print("Skriv A, B eller C.")

		if val == ratt_svar:
			print("Rätt svar!")
			poang += 1
		else:
			print(f"Fel svar. Rätt svar är {ratt_svar}.")

	print(f"\nResultat: {poang} av {len(fragor)} rätt på {niva} nivå.")


if __name__ == "__main__":
	while True:
		spela()
		if input("Vill du spela igen? (j/n): ").strip().lower() not in ("j", "ja"):
			print("Tack för att du spelade!")
			break
