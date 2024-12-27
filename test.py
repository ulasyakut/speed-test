import streamlit as st
import speedtest 
import datetime

st.header("Speed Test")

test = speedtest.Speedtest()

if st.button('Start Speed Test'):

    st.write('Please wait...')
    best_server = test.get_best_server()
    st.write(f'Best server is {best_server['host']} from {best_server['country']}')


  
    download = test.download()/1000000
    upload = test.upload()/1000000
    ping = test.results.ping
    time = datetime.datetime.now()
    
    st.write(f'Your download speed is {download:.2f} upload is {upload:.2f} and ping is {ping:.0f}')
    st.write(f'Time is: {time}')

    data = [download,upload,ping,time]

    csv_data = "Download Speed,Upload Speed,Ping,Time\n"
    csv_data += f"{download:.2f},{upload:.2f},{ping:.0f},{time}"

    st.download_button(label="Download", data=csv_data, file_name="speed_test_records.csv", mime="text/csv")

