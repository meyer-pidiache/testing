using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Parcial2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private bool esPar(double numero)
        {
            return (numero % 2 == 0);
        }

        private void sumar()
        {
            double numero1 = Convert.ToDouble(numericUpDown1.Value);
            double numero2 = Convert.ToDouble(numericUpDown2.Value);
            double resultado = numero1 + numero2;

            labelResultadoSuma.Text = Convert.ToString(resultado);

            labelResultado.Text = esPar(resultado) ? "Par" : "Impar";
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            labelNumero1.Text = esPar(Convert.ToDouble(numericUpDown1.Value)) ? "Par" : "Impar";
            sumar();
        }

        private void numericUpDown2_ValueChanged(object sender, EventArgs e)
        {
            labelNumero2.Text = esPar(Convert.ToDouble(numericUpDown2.Value)) ? "Par" : "Impar";
            sumar();
        }
    }
}
