#!/usr/bin/env python

from PIL import Image


#Assume all images passed into the list are the same size
class img_merger():
	def __init__(self, plot_path_list, crop_window=None, horizontal=True):
		self.plot_path_list = plot_path_list
		self.num_of_plots = len(plot_path_list)
		self.crop_window = crop_window
		self.horizontal = horizontal
		self.img_list = []

		self.open_all_images()
		self.crop_img()
		self.size = self.img_list[0].size

		exec('self.merge_' + str(self.num_of_plots) + '()')

	def open_all_images(self):
		for pth in self.plot_path_list:
			im = Image.open(pth)
			self.img_list.append(im)


	def crop_img(self):
		if self.crop_window is None: return
		for idx, img in enumerate(self.img_list):
			self.img_list[idx] = img.crop(self.crop_window)


	def show_img(self):
		self.output_img.show()

	def merge_2(self):
		if self.horizontal:
			new_width = 2*self.size[0]
			new_height = self.size[1]
	
			Horiz_img = Image.new('RGB', (new_width, new_height))
			Horiz_img.paste(self.img_list[0], (0,0))
			Horiz_img.paste(self.img_list[1], (self.size[0],0))
	
			self.output_img = Horiz_img
		else:
			new_width = self.size[0]
			new_height = 2*self.size[1]
	
			vert_img = Image.new('RGB', (new_width, new_height))
			vert_img.paste(self.img_list[0], (0,0))
			vert_img.paste(self.img_list[1], (0,self.size[1]))
	
			self.output_img = vert_img


	def merge_3(self):
		if self.horizontal:
			new_width = 3*self.size[0]
			new_height = self.size[1]
	
			Horiz_img = Image.new('RGB', (new_width, new_height))
			Horiz_img.paste(self.img_list[0], (0,0))
			Horiz_img.paste(self.img_list[1], (self.size[0],0))
			Horiz_img.paste(self.img_list[2], (2*self.size[0],0))
	
			self.output_img = Horiz_img
		else:
			new_width = self.size[0]
			new_height = 3*self.size[1]
	
			vert_img = Image.new('RGB', (new_width, new_height))
			vert_img.paste(self.img_list[0], (0,0))
			vert_img.paste(self.img_list[1], (0,self.size[1]))
			vert_img.paste(self.img_list[2], (0,2*self.size[1]))
	
			self.output_img = vert_img

	def merge_4(self):
		new_width = 2*self.size[0]
		new_height = 2*self.size[1]

		Horiz_img = Image.new('RGB', (new_width, new_height))
		Horiz_img.paste(self.img_list[0], (0,0))
		Horiz_img.paste(self.img_list[1], (self.size[0],0))
		Horiz_img.paste(self.img_list[2], (0, self.size[1]))
		Horiz_img.paste(self.img_list[3], (self.size[0], self.size[1]))

		self.output_img = Horiz_img


	def merge_5(self):
		img_w = self.size[0]
		img_h = self.size[1]

		new_width = 3*img_w
		new_height = 2*img_h

		Horiz_img = Image.new('RGB', (new_width, new_height), 'WHITE')
		Horiz_img.paste(self.img_list[0], (0,0))
		Horiz_img.paste(self.img_list[1], (img_w,0))
		Horiz_img.paste(self.img_list[2], (2*img_w,0))
		Horiz_img.paste(self.img_list[3], (int(img_w/2.0), img_h))
		Horiz_img.paste(self.img_list[4], (int(3*img_w/2.0), img_h))

		self.output_img = Horiz_img

	def merge_6(self):
		img_w = self.size[0]
		img_h = self.size[1]

		new_width = 3*img_w
		new_height = 2*img_h

		Horiz_img = Image.new('RGB', (new_width, new_height), 'WHITE')
		Horiz_img.paste(self.img_list[0], (0,0))
		Horiz_img.paste(self.img_list[1], (img_w,0))
		Horiz_img.paste(self.img_list[2], (2*img_w,0))
		Horiz_img.paste(self.img_list[3], (0, img_h))
		Horiz_img.paste(self.img_list[4], (img_w, img_h))
		Horiz_img.paste(self.img_list[5], (2*img_w, img_h))

		self.output_img = Horiz_img


	def save_img(self, output_path):
		pass

if __name__ == "__main__":

	img_path_list = []
	img_path_list.append("wine/wine_10/kernel_1.png")
	img_path_list.append("wine/wine_10/kernel_2.png")
	img_path_list.append("wine/wine_10/kernel_3.png")
	img_path_list.append("wine/wine_10/kernel_4.png")
	img_path_list.append("wine/wine_10/kernel_5.png")
	img_path_list.append("wine/wine_10/kernel_6.png")
	imSize = Image.open(img_path_list[0]).size
	crop_window = (80, 20,imSize[0] - 80, imSize[1] - 5)

	Imerger = img_merger(img_path_list, crop_window)
	Imerger.show_img()






#new_im = Image.new('RGB', (1000,1000))
#
#im2 = Image.open("wine/wine_1/kernel_2.png")
#shp = im2.size
#imCrop2 = im2.crop((80, 20,shp[0] - 80, shp[1] - 5))
#
#
#im = Image.open("wine/wine_1/kernel_1.png")
#shp = im.size
#imCrop = im.crop((80, 20,shp[0] - 80, shp[1] - 5))
#shp2 = imCrop.size
#
#new_im.paste(imCrop, (0,0))
#new_im.paste(imCrop2, (480,0))
#
#new_im.show()
