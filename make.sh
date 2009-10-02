export TEXINPUTS="./share/styles//:"
export TEXFONTS="./share/fonts//:"

src='hw3'
for i in 1 2; do
	latex ${src}.tex
done
dvips ${src}.dvi -o
ps2pdf ${src}.ps
