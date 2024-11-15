def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm."
        else:
            return "Phương trình vô nghiệm."
    else:
        x = -b / a
        return f"Phương trình có nghiệm x = {x:.2f}"
