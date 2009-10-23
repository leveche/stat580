export TEXINPUTS="./share/styles//:"
export TEXFONTS="./share/fonts//:"

case $1 in
	'clean')
		mv *.ps *dvi *.aux *.log *.pdf *.end /tmp;
	;;
	*)
		src=$1	#'hw5'
		for i in 1 2; do
			latex ${src}.tex
			pdflatex ${src}.tex
		done
		#dvips ${src}.dvi -o
		#ps2pdf ${src}.ps
		open ${src}.pdf
esac
