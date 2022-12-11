data = {'192.168.1.2': ('CVE-2016-8743', '2.2.32'),
        '192.168.1.12': ('CVE-2018-1283', '2.4.0'),
        '192.168.1.200': ('CVE-2022-23943', '2.4.52'),
        '192.168.1.5': ('CVE-2016-5387', '2.4.23')
        }
print("\n".join(str(elem)[1:-1] for elem in (sorted(data.items(), key=lambda items: tuple(items[1][1]), reverse=True))))
