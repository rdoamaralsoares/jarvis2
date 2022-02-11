import qrcode
from qrcode.constants import ERROR_CORRECT_H, ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q

class WiFi_QR_Code:
#__init__ method:
    def __init__(self, error_correction: int = None, box_size: int = None, border: int = None) -> None:
        
        #Set default values if not provided:
        if error_correction == None:
            error_correction = ERROR_CORRECT_L
        if box_size == None:
            box_size = 1
        if border == None:
            border = 4

        if border < 4:
            #Print error for a border below minimum specification
            print(''.join(['Error: ', str(border), 'px border is lower than the 4px minimum']))
            exit()

        if error_correction not in range(4):
            #Print error message for an invalid 'error_correction' level:
            print(''.join(['Error: error correction level ', str(error_correction), ' is not in range 0-3']))
            exit()
        
        #Setup QR code object: 
        self.qr_code = qrcode.QRCode(
            error_correction = error_correction,
            box_size = box_size,
            border = border
        )
    
    #Method for appending file type extension to filename:
    def __filetype_substring__(self, file_name: str, file_type: str) -> str: 

        #Add extension prefix:
        if file_type[0] != '.':
            file_type = ''.join(['.', str(file_type)])
        
        #Check for extension ending:
        if file_name[len(file_name) - len(file_type):] != file_type:
            file_name = ''.join([str(file_name), file_type])
            print(file_name)
        
        #Return filename:
        return file_name
        
    #Encode WiFi method:
    def encode_wifi(self, ssid: str, password: str, encryption: str = None, hidden: str = None) -> str:
        #Store current SSID:
        self.ssid = ssid

        #Set default values if not provided:
        if encryption == None:
            encryption = 'WPA'
        if hidden == None:
            hidden = False

        #Encode WiFi credentials in legal format:
        wifi_metadata = ''.join([
            'WIFI:T:', str(encryption),
            ';S:', str(ssid),
            ';P:', str(password),
            ';H:', str(hidden)
            ])
        
        #Return encoded Wifi credentials:
        return wifi_metadata

    def generate_wifi_qrcode(self, wifi_metadata: str, file_name: str, file_directory: str = None, fill_color: tuple = None, back_color: tuple = None) -> str:
        #Append PNG filetype if not included:
        file_name = self.__filetype_substring__(file_name, 'png')

        #Set default values if not provided:
        if file_directory == None:
            file_directory = ''
        if fill_color == None:
            fill_color = 'black'
        if back_color == None:
            back_color = 'white'
        
        if fill_color == back_color:
            #Print error for QR code fill color and background color being equal:
            print(''.join(['Error: QR code fill color and back color are the same']))
            exit()

        #Add WiFi metadeta to QR code:
        self.qr_code.add_data(wifi_metadata)
        #Compile the data into a QR code array:
        self.qr_code.make(fit = True)
        #Generate an image from QR code data, provide color:
        wifi_qrcode = self.qr_code.make_image(fill_color = fill_color,
                                              back_color = back_color)
        #Save QR code with the specified file name in a  file directory:
        file_directory = ''.join([file_directory, file_name])
        wifi_qrcode.save(file_directory)

        #Return directory of the saved file:
        return file_directory
        

#definir qual será o SSID que será usado
ssid = 'IOT'
password = '<YOUR PASSWORD>'

QR_WiFi = WiFi_QR_Code(error_correction = ERROR_CORRECT_L,
                       box_size = 20,
                       border = 4)
                       


#Encode WiFi credentials into raw_wifi string:
raw_wifi = QR_WiFi.encode_wifi(
    ssid = ssid,
    password = password,
    encryption = 'WPA',
    hidden = False
    )


#Generate the WiFi QR code:
file_location = QR_WiFi.generate_wifi_qrcode(
    wifi_metadata = raw_wifi,
    file_name = 'WiFi_QR_Code-NTT.png',
    fill_color = (0, 0, 0),
    back_color = (255, 255, 255)
    )

#Print SSID and file location:
print(''.join(['WiFI QR Code file location | with SSID: ', QR_WiFi.ssid, '\n', file_location]))
