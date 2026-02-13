import streamlit as st
import hashlib
import requests 

def check_pwned_password(password):
    sha1_hash=hashlib.sha1(password.encode()).hexdigest()
    sha1_hash=sha1_hash.upper()
    prefix=sha1_hash[:5]
    url=f"https://api.pwnedpasswords.com/range/{prefix}"
    response=requests.get(url,timeout=10)
    response.raise_for_status()
    return response.text,sha1_hash

#naslov aplikacije
st.title("Provjera sigurnosti lozinke")

#Unos lozinke
password=st.text_input("Unesi lozinku: ",type="password")

#Gumb za provjeru
if st.button("Provjeri sigurnost"):
    if password:
         
        has_upper=any(znak.isupper()for znak in password)
        has_lower=any(znak.islower()for znak in password)
        has_digit=any(znak.isdigit()for znak in password)
        has_special = any(znak in "!@#$%^&*()_+-=[]{}|;:,.<>?" for znak in password)
        #Bodovanje za duljinu lozinke( max 30)
        score=0
        if len(password)>=12:
            score+=30
        elif len(password)>=8:
            score+=20
        elif len(password)>=6:
            score+=10
        
        #Bodovi za znakove
        if has_upper:
            score+=15
        if has_lower:
            score+=15
        if has_digit:
            score+=15
        if has_special:
            score+=25
        #Prikaz rezultata
        st.subheader("Rezultati provjere: ")
        st.write(f" ✅ Velika slova: {'DA' if has_upper else 'NE'}")
        st.write(f" ✅ Mala slova: {'DA' if has_lower else 'NE'}")
        st.write(f" ✅ Brojevi: {'DA' if has_digit else 'NE'}")
        st.write(f" ✅ Specijalni znakovi: {'DA' if has_special else 'NE'}")
        st.write("---")
        st.subheader(f"Ocijena: {score}/100")

        #Progres bar
        st.progress(score/100)  

        #Poruke prema ocijeni
        if score>=80:
            st.success("Odlična lozinka! Vrlo sigurna.")
        elif score>=60:
            st.info("Dobra lozinka, ali može biti bolja.")
        elif score>=40:
            st.warning("Slaba lozinka.Preporučujmo poboljšanje.")
        else:
            st.error("Vrlo slaba lozinka! Hitno promijeni!")
            
        st.write("---")
        st.subheader("Sigurnost lozinke prema API-ju Pwned Passwords:")

        with st.spinner("Provjeravam sigurnost lozinke..."):
            try:
                api_response,full_hash=check_pwned_password(password)
            except requests.exceptions.RequestException as e:
                st.error(f"Greška pri spajanju na API: {e}")
            else:
                suffix=full_hash[5:]
                found_count=None

                for line in api_response.splitlines():
                    if line.startswith(suffix+":"):
                        found_count=int(line.split(":")[1])
                        break
                if found_count is not None:
                    st.error(f"Lozinka je pronađena {found_count} puta u bazi podataka.")
                    st.warning("Promijeni lozinku odmah!")
                else:
                    st.success("Lozinka nije pronađena u bazi podataka.")  

        
    else:
        st.write("Nisi unio lozinku")
    st.write("---")
    st.write("Ovaj alat je napravljen u svrhu edukacije i podizanja svijesti o sigurnosti lozinki.")
    st.write("Ne preporucuje se koristenje alata sa lozinkama koje se koriste na drugim platformama.")
    st.write("Za vise informacija posjetite: https://haveibeenpwned.com/")
    st.write("---")
    st.write("Powered by Filip (20% Digital)")
    