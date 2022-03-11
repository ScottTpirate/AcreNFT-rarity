import streamlit as st
import urllib.request
import json
from PIL import Image
import qrcode 


# https://ipfs.io/ipfs/


def showAttributes(number):
    with open('rarity_scores.json') as f:
        json_data = json.loads(f.read())
        for i in json_data:
            if i["edition"] == int(number):
                data = i

        edition = data['edition']
        rarity = data['rarity_score']
        rank = data['rank']
        col2.subheader(f"Edition: `{edition}`")
        # st.sidebar.write(data['edition'])
        col2.subheader(f"Rarity Score: `{rarity}`")
        col2.subheader(f"Rarity Rank: `{rank}`")
        
        for a in data['attributes']:
            trait_type = a['trait_type']
            value = a['value']
            occurence = a['occurence']
            elements.markdown(f"**{trait_type}** : `{value}` ")
            o = float(a['occurence'][:-1])
            elements.write(f"Trait Rarity: `{occurence}`")
            elements.progress(int(o))

        element3.write(data)



numba = st.sidebar.text_input('Acre NFT #')


col1, col2 = st.columns(2)
elements = st.container()
element2 = st.expander("Raw json NFT")
element3 = st.expander("Raw json rarity")



if numba:
    if int(numba) in range(1,4841, 1):

        with st.spinner(text='In progress'):
            
            nftURL = f'https://ipfs.io/ipfs/bafybeieddquuzqtgctyeoqt3rtfip775u5dkkbbpk4xcmquxd3kjwkz6ye/galaxyut8PuH/{numba}'
            r = urllib.request.urlopen(nftURL)
            body = r.read().decode()
            todo_item = json.loads(body)

            img_url = todo_item['image']
            # print(img_url[7:])

            element2.write(todo_item)
            showAttributes(numba)

            qr_img = qrcode.make(nftURL)
            # qr_img.size(300,300)
            qr_img.save("qr.png")
            # qr = qr_img.tobytes("hex", "rgb")
            qr = Image.open("qr.png")
            qr = qr.resize((100, 100))
            col2.image(qr)


        with col1:
            with st.spinner(text='Loading Image'):
                im = urllib.request.urlopen(f'https://ipfs.io/ipfs/{img_url[7:]}')

                img = Image.open(im)

                col1.image(img)
        
            
            


