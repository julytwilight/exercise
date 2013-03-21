require 'mini_magick'

dir_name =  File.dirname(__FILE__)

def compress_img(file, limit)
  img = MiniMagick::Image.open(file)
  width, height = img[:width].to_f, img["height"].to_f

  rate = (width > height) ? (height / limit) : (width / limit)

  n_width = width / rate
  n_height = height / rate

  img.resize "#{n_width}x#{n_height}"

  if width > height
    shave = (n_width - limit) / 2
    img.shave("#{shave}x0")
  else
    shave = (n_height - limit) / 2
    img.shave("0x#{shave}")
  end
  name = file.split('.')
  img.write "#{name[0]}_#{limit}.#{name[1]}"
end

Dir.foreach(dir_name) do |f|
  name = f.split('.')
  if ['jpg', 'png', 'jpge', 'gif'].include? name[1]
    compress_img(f, 200)
    compress_img(f, 80)
  end
end