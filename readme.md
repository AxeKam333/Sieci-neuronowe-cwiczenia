# Weka

3. Największy wpływ mają:

higher
schoolsup
failures


4. wybrane atrybuty: (posortowane jak w plikach)
age
Medu
Fedu
studytime
failures
schoolsup
higher
absences

dla testów na przefiltrowanych danych: wpływ ma tylko minNumObj, przy wartości 10 daje wynik 61,5385%

5. minNumObj na 10 i binarySplit na False daje lepsze wyniki: 63,0769

6. Drzewo w math jest malutkie, w portugalskim gigantyczne
w obu jest podział wg schoolsup (w math jest to 2 atrybut do podziału, w por 4)
health dzieli na te <=1 a >1

7.
w por
failures <= 0
|   higher = yes
|   |   school = GP
|   |   |   schoolsup = no
|   |   |   |   Walc > 3
|   |   |   |   |   Fjob = teacher: '(11.5-inf)' (2.0)

w math to będzie 
failures <= 1
schoolsup = no
age <= 16
sex = F
healtyh <= 1

jeżeli do tej pory ktoś zdawał raczej wszystko 
i nie potrzebował dodatkowych zajęć to jest duża szansa że zda - jest uważnym i pilnym uczniem.


//notatki:

algorytm: C45
J48 przyczytać

żeby porównać z PRISM wykonaj dyskretyzacje: Preprocessing>filtres>supervised>Discretise