# Module  
pip install mypy - sucht Fehler mit typing(TypeAnnotation)
import typing:
SupportFloat: int or float
Union: mehrere Datentypen -> oder Verknüpfung -> Union(int, str,...)
-------
NewType: neuer Typ ... Name = NewType('Name', str)
TypeVar .. neuer Typ bei dem mehrere Möglichkeiten gibt: TypeVar('T', str, int, float)
--------
Callable .. Funktion die aufgerufen wird (__cal__ objekt implementiert bei Klassen,
                                    methoden haben es immer!!) 
                1.Bsp: Callable[..., List[int]] -> "..." ist egal
                1.Para: Parameter
                2.Para: return

                2.Bsp: Callable[[para1, para2], return]
Optional[List[int]] <=> Union[List[int], None]
Optional .. Optional[List[int]]: entweder Typ oder None
            interessant für Listen, da nie [] übergeben werden sollen
Dict[key, value] ... Dictionary mit speziellem key, value
Mapping[key, value]: wenn kein explizites Dict übergeben wird

List

mypy ist noch relativ neu: findet nicht alles oder bringt Fehler die nicht zwingend Fehler sind
allgemein ist typeAnnotation noch recht neu, wird in zukünfitgen Version sicher verbessert
