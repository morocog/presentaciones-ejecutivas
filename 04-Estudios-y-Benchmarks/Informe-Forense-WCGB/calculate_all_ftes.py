import openpyxl
from datetime import datetime
from collections import defaultdict

wb = openpyxl.load_workbook('WCGB_Billable_Hours_2021.xlsx', data_only=True)

daily_records = []

for sheet_name in ['November Daily Hrs', 'December Daily Hrs']:
    ws = wb[sheet_name]
    rows = list(ws.iter_rows(values_only=True))
    date_row = rows[3]
    
    date_cols = []
    for c_idx, val in enumerate(date_row):
        if c_idx >= 5 and val is not None:
            if isinstance(val, datetime):
                dt_str = val.strftime('%Y-%m-%d')
                date_cols.append((c_idx, dt_str, val))
            elif '2021' in str(val):
                dt_str = str(val)[:10]
                date_cols.append((c_idx, dt_str, datetime.strptime(dt_str, '%Y-%m-%d')))
                
    for c_idx, dt_str, dt_obj in date_cols:
        total_hrs_all = 0.0
        total_hrs_mx = 0.0
        hc_all = 0
        hc_mex = 0
        training_hrs_mx = 0.0
        prod_hrs_mx = 0.0
        
        for r in rows[4:]:
            if not r or len(r) <= c_idx:
                continue
            name = r[1]
            loc = str(r[2] or '').strip()
            val = r[c_idx]
            if val is not None:
                try:
                    val_f = float(val)
                    if val_f > 0:
                        total_hrs_all += val_f
                        hc_all += 1
                        if loc == 'MX':
                            total_hrs_mx += val_f
                            hc_mex += 1
                            # Check if it was 8.000000000058208 (training)
                            if abs(val_f - 8.0) < 0.001 and sheet_name == 'November Daily Hrs':
                                training_hrs_mx += val_f
                            else:
                                prod_hrs_mx += val_f
                except:
                    pass
        
        daily_records.append({
            'date': dt_str,
            'datetime': dt_obj,
            'week_num': dt_obj.isocalendar()[1],
            'total_hrs_mx': total_hrs_mx,
            'hc_mex': hc_mex,
            'daily_fte_mx': total_hrs_mx / 8.0,
            'total_hrs_all': total_hrs_all,
            'hc_all': hc_all,
            'daily_fte_all': total_hrs_all / 8.0
        })

print("==========================================================================================")
print("                    AUDITORÍA 2021: DIARIO (MÉXICO Y TOTAL)")
print("==========================================================================================")
print(f"{'Fecha':<12} | {'Día':<4} | {'Sem':<4} | {'HC MX':<6} | {'Horas MX':<10} | {'FTE Diario MX (8h)':<18} | {'HC Global':<9} | {'FTE Global':<10}")
print("-" * 90)

days_map = {0: 'Lun', 1: 'Mar', 2: 'Mié', 3: 'Jue', 4: 'Vie', 5: 'Sáb', 6: 'Dom'}

for rec in sorted(daily_records, key=lambda x: x['datetime']):
    dow = days_map[rec['datetime'].weekday()]
    print(f"{rec['date']:<12} | {dow:<4} | W{rec['week_num']:<3} | {rec['hc_mex']:<6} | {rec['total_hrs_mx']:<10.2f} | {rec['daily_fte_mx']:<18.2f} | {rec['hc_all']:<9} | {rec['daily_fte_all']:<10.2f}")

print("\n==========================================================================================")
print("                    AUDITORÍA 2021: RESUMEN SEMANAL (FTE = 40 HORAS)")
print("==========================================================================================")
print(f"{'Semana ISO':<12} | {'Rango de Fechas':<23} | {'HC Activo MX':<13} | {'Horas MX':<10} | {'FTE Semanal MX (40h)':<20} | {'Horas Global':<12} | {'FTE Global (40h)':<16}")
print("-" * 105)

weeks = defaultdict(list)
for rec in daily_records:
    weeks[rec['week_num']].append(rec)

for w_num in sorted(weeks.keys()):
    recs = weeks[w_num]
    min_date = min(r['date'] for r in recs)
    max_date = max(r['date'] for r in recs)
    tot_hrs_mx = sum(r['total_hrs_mx'] for r in recs)
    tot_hrs_all = sum(r['total_hrs_all'] for r in recs)
    # Peak daily HC in week
    peak_hc_mx = max(r['hc_mex'] for r in recs)
    weekly_fte_mx = tot_hrs_mx / 40.0
    weekly_fte_all = tot_hrs_all / 40.0
    print(f"Semana {w_num:<5} | {min_date} al {max_date} | {peak_hc_mx:<13} | {tot_hrs_mx:<10.2f} | {weekly_fte_mx:<20.2f} | {tot_hrs_all:<12.2f} | {weekly_fte_all:<16.2f}")
