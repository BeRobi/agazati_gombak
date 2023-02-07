import szam
import korok

korok_lista = korok.beker()
szam.vel_szam()

print("\nII/A, B, C:")
f"\t{korok.osszefuz(korok_lista, ' : ')}"
print("\nII/D, E:")
korok.konzolra_ir(korok_lista)
print("\nII/F:")
korok.fajl_ir(korok_lista)

korok.beolvas()
gombafajtak = korok.beolvas()
korok.gombak_szama(gombafajtak)
korok.papsapka(gombafajtak)
korok.tinoru(gombafajtak)
