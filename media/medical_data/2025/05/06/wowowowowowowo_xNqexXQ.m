clear all
x=[1,2,3,4,5] %zde nemuze byt karel;
A={1,2,3,4,'karel'} %zde muze byt karel;
A(1);
A{1};

%struktury
%jako databaze v matlabu, otevrete pacienti v promenych vypada jako excel
pacienti(1).jmeno="Mrs green";
pacienti(1).vek=29;
pacienti(1).FL=60;
pacienti(2).jmeno="Mrs black";
pacienti(2).vek=32;
pacienti(2).FL=31;
pacienti(3).jmeno="Mrs white";
pacienti(3).vek=35;
pacienti(3).FL=72;
pacienti(4).jmeno="Mrs blue";
pacienti(4).vek=25;
pacienti(4).FL=25;
pacienti(5).jmeno="Mrs purple";
pacienti(5).vek=30;
pacienti(5).FL=62;

vel=size(pacienti) %velikost struktury
for i=1:vel(2) %nova hodnota "plod" do tabulky
    pacienti(i).plod=pacienti(i).FL*7
end

for i=1:vel(2) %nova hodnota info do tabulky
    if pacienti(i).plod <= 420
        pacienti(i).info="2nd trimester"
    else 
        pacienti(i).info="3nd trimester"
    end
end