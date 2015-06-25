from sys import version_info

py3 = version_info[0] > 2
if py3:
	gallery = input("Which gallery do you want to add to? ")
else:
	gallery = raw_input("Which gallery do you want to add to? ")

outname = 'gallery/'+ gallery + '.html'
fwrite = open(outname, 'w')

fwrite.write('<!DOCTYPE html>\n<html lang="en">\n\n<head>\n')
fwrite.write('    <title>where\'s jackie at - ' + gallery + '</title>\n')

header = open('js/template/gallery_header.html', 'r')
fwrite.write(header.read())
fwrite.write('\n\n')

if gallery == "Vivian":
	pageTitle = "Vivian &amp; Jose"
elif gallery == "Portland":
	pageTitle = "Portland, OR"
elif gallery == "Seattle":
	pageTitle = "Seattle, WA"
elif gallery == "Vancouver":
	pageTitle = "Vancouver, BC"

fwrite.write('            <div class="col-lg-12">\n')
fwrite.write('                <h1 class="page-header">' + pageTitle + '</h1>\n')
fwrite.write('            </div>\n')

fname = 'gallery/photogen/' + gallery + '.txt'
with open(fname, 'r') as fopen:
	while True:
		if gallery == "Vivian":
			picViv = fopen.readline().rstrip('\n')
		picNum = fopen.readline().rstrip('\n')
		if not picNum: break
		picURL = fopen.readline().rstrip('\n')
		picLarge = fopen.readline().rstrip('\n')
		picTitle = fopen.readline().rstrip('\n')
		picDesc = fopen.readline().rstrip('\n')
		fopen.readline()

		if gallery == "Vivian":
			thumb = "../assets/thumb/201506_PNW/" + picViv + "/DSC_" + picNum + ".jpg"
		else:
			thumb = "../assets/thumb/201506_PNW/" + gallery + "/DSC_" + picNum + ".jpg"
		print thumb

		html = '            <div class="col-lg-3 col-md-4 col-xs-6 thumb">\n'
		html += '                <a class="thumbnail" href="#">\n'
		html += '                    <img class="img-responsive" src="' + thumb
		html += '" alt="" data-toggle="modal" data-target="#' + picNum + '">\n'
		html += '                </a>\n'
		html += '            </div>\n\n'
		html += '            <!-- Modal -->\n'
		html += '            <div id="'+ picNum + '" class="modal fade" role="dialog">\n'
		html += '              <div class="modal-dialog">\n\n'
		html += '                <!-- Modal content-->\n'
		html += '                <div class="modal-content">\n'
		html += '                  <div class="modal-body">\n'
		html += '                    <button type="button" class="close" data-dismiss="modal">&times;</button>\n'
		html += '                    <a href="' + picLarge + '">\n'
		html += '                      <img class="full-img" src="' + picURL + '" />\n'
		html += '                    </a>\n'
		html += '                  </div>\n'
		html += '                  <div class="modal-footer">\n'
		if picTitle != "NA":
			html += '                    <h4 class="modal-title">' + picTitle + '</h4>\n'
		if picDesc != "NA":
			html += '                    <p class="modal-desc">' + picDesc + '</p>\n'
		html += '            </div></div></div></div>\n\n\n'

		fwrite.write(html)

fwrite.write('    </div></div>')
footer = open('js/template/general_footer.html', 'r')
fwrite.write(footer.read())

header.close()
footer.close()
fopen.close()
fwrite.close()