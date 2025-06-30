# ماژول بلاک اکسپلورر و API برای PersianChain
# نویسنده: Mohammad Nasser Haji Hashemabad
# توضیحات: این ماژول یک API ساده برای مشاهده بلاک‌ها، تراکنش‌ها و حساب‌ها فراهم می‌کند.
# برای اجرا: pip install flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# داده‌های نمونه (در پروژه واقعی باید به بلاکچین و ماژول‌های دیگر متصل شود)
بلاک_ها = [
    {"شماره": 0, "تراکنش_ها": [], "هش": "000..."},
    {"شماره": 1, "تراکنش_ها": [{"فرستنده": "A", "گیرنده": "B", "مقدار": 10}], "هش": "abc..."}
]
تراکنش_ها = [
    {"فرستنده": "A", "گیرنده": "B", "مقدار": 10},
    {"فرستنده": "B", "گیرنده": "C", "مقدار": 5}
]
حساب_ها = {
    "A": 90,
    "B": 55,
    "C": 5
}

@app.route("/بلاک‌ها", methods=["GET"])
def دریافت_بلاک_ها():
    return jsonify(بلاک_ها)

@app.route("/تراکنش‌ها", methods=["GET"])
def دریافت_تراکنش_ها():
    return jsonify(تراکنش_ها)

@app.route("/حساب‌ها", methods=["GET"])
def دریافت_حساب_ها():
    return jsonify(حساب_ها)

@app.route("/افزودن_تراکنش", methods=["POST"])
def افزودن_تراکنش():
    داده = request.get_json()
    تراکنش_ها.append(داده)
    return jsonify({"وضعیت": "تراکنش افزوده شد"}), 201

if __name__ == "__main__":
    app.run(port=8000, debug=True) 