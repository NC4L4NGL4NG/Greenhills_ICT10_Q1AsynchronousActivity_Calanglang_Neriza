
if __name__ == '__main__':
    html_content = build_page()
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("contact.html has been created. Open it in your browser.")

