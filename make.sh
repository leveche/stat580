export TEXINPUTS="./share/styles//:"
export TEXFONTS="./share/fonts//:"

#RVC='./random-walk-code.tex' 
#rm $RVC -f
#echo '\begin{verbatim}' > $RVC
#cat ./hw1q3.py >> $RVC
#echo '\end{verbatim}' >> $RVC

src='hw1'
for i in 1 2; do
	latex ${src}.tex
done
dvips ${src}.dvi -o
ps2pdf ${src}.ps
